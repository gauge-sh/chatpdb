import os
from typing import Iterable, Literal

from openai import OpenAI
from pydantic import BaseModel
from tenacity import retry, stop_after_attempt, wait_random_exponential


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY") or os.environ.get("CHATPDB_OPENAI_API_KEY")
)


def get_model() -> str:
    return os.environ.get("OPENAI_MODEL") or os.environ.get(
        "CHATPDB_OPENAI_MODEL", "gpt-4.5-turbo"
    )


class OpenAIMessage(BaseModel):
    role: Literal["user"] | Literal["system"] | Literal["assistant"]
    content: str

    @classmethod
    def system_prompt(cls, content: str) -> "OpenAIMessage":
        return cls(role="system", content=content)

    @classmethod
    def user_message(cls, content: str) -> "OpenAIMessage":
        return cls(role="user", content=content)


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(4))
def prompt(messages: list[OpenAIMessage]) -> str:
    if not messages:
        raise ValueError("messages must not be empty for OpenAI prompt")
    response = client.chat.completions.create(
        messages=[message.model_dump() for message in messages],
        model=get_model(),
    )
    return response.choices[0].message.content


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(4))
def prompt_streaming(messages: list[OpenAIMessage]) -> Iterable[str]:
    if not messages:
        raise ValueError("messages must not be empty for OpenAI prompt")
    completion_stream = client.chat.completions.create(
        messages=[message.model_dump() for message in messages],
        model=get_model(),
        stream=True,
    )
    return (chunk.choices[0].delta.content for chunk in completion_stream)
