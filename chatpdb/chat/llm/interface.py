from enum import Enum
from typing import Iterable


class LLMBackend(Enum):
    OPENAI = "openai"


def prompt(prompt_input: str, backend: LLMBackend = LLMBackend.OPENAI) -> str:
    if backend == LLMBackend.OPENAI:
        from chatpdb.chat.llm.openai import prompt as openai_prompt, OpenAIMessage

        return openai_prompt([OpenAIMessage(role="user", content=prompt_input)])
    else:
        raise NotImplementedError(f"Backend {backend} is not implemented")


def prompt_streaming(
    prompt_input: str, backend: LLMBackend = LLMBackend.OPENAI
) -> Iterable[str]:
    if backend == LLMBackend.OPENAI:
        from chatpdb.chat.llm.openai import (
            prompt_streaming as openai_prompt_streaming,
            OpenAIMessage,
        )

        return openai_prompt_streaming(
            [OpenAIMessage(role="user", content=prompt_input)]
        )
    else:
        raise NotImplementedError(f"Backend {backend} is not implemented")
