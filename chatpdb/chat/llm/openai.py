import os
from typing import Iterable, Literal, List, Union

from openai import OpenAI
from pydantic import BaseModel


def get_client() -> OpenAI:
    api_key = os.environ.get("CHAT_PDB_OPENAI_API_KEY") or os.environ.get(
        "OPENAI_API_KEY"
    )
    organization = os.environ.get("CHAT_PDB_OPENAI_ORG_ID") or os.environ.get(
        "OPENAI_ORG_ID"
    )
    if not api_key:
        raise ValueError("OpenAI API key not set")
    return OpenAI(api_key=api_key, organization=organization)


def get_model() -> str:
    return os.environ.get("CHAT_PDB_OPENAI_MODEL") or os.environ.get(
        "OPENAI_MODEL", "gpt-4-turbo"
    )


class OpenAIMessage(BaseModel):
    role: Union[Literal["user"], Literal["system"], Literal["assistant"]]
    content: str

    @classmethod
    def system_prompt(cls, content: str) -> "OpenAIMessage":
        return cls(role="system", content=content)

    @classmethod
    def user_message(cls, content: str) -> "OpenAIMessage":
        return cls(role="user", content=content)


def prompt(messages: List[OpenAIMessage]) -> str:
    if not messages:
        raise ValueError("messages must not be empty for OpenAI prompt")
    response = get_client().chat.completions.create(
        messages=[message.model_dump() for message in messages],  # type: ignore
        model=get_model(),
    )
    return response.choices[0].message.content  # type: ignore


def prompt_streaming(messages: List[OpenAIMessage]) -> Iterable[str]:
    if not messages:
        raise ValueError("messages must not be empty for OpenAI prompt")
    completion_stream = get_client().chat.completions.create(  # type: ignore
        messages=[message.model_dump() for message in messages],  # type: ignore
        model=get_model(),
        stream=True,
    )
    return (chunk.choices[0].delta.content or "" for chunk in completion_stream)
