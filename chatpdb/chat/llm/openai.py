import os
from typing import Iterable, Literal

from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY") or os.environ.get("CHATPDB_OPENAI_API_KEY")
)


def get_model() -> str:
    return os.environ.get("OPENAI_MODEL") or os.environ.get(
        "CHATPDB_OPENAI_MODEL", "gpt-4.5-turbo"
    )


class OpenAIMessage(BaseModel):
    role: Literal["user"] | Literal["system"]
    content: str


def prompt(messages: list[OpenAIMessage]) -> str:
    if not messages:
        raise ValueError("messages must not be empty for OpenAI prompt")
    response = client.chat.completions.create(
        messages=[message.model_dump() for message in messages],
        model=get_model(),
    )
    return response.choices[0].message.content


def prompt_streaming(messages: list[OpenAIMessage]) -> Iterable[str]:
    if not messages:
        raise ValueError("messages must not be empty for OpenAI prompt")
    completion_stream = client.chat.completions.create(
        messages=[message.model_dump() for message in messages],
        model=get_model(),
        stream=True,
    )
    return (chunk.choices[0].delta.content for chunk in completion_stream)
