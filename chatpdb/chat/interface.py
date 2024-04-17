import traceback
from typing import Iterable

from pydantic import BaseModel

from chatpdb.chat.llm import prompt_streaming
from chatpdb.chat.prompts import get_ask_prompt, get_explain_prompt


class AskArgs(BaseModel):
    message: str
    stack_trace: list[traceback.FrameSummary]
    local_vars: dict[str, str]
    global_vars: dict[str, str]
    exception: str = ""

    class Config:
        arbitrary_types_allowed = True


def ask(args: AskArgs) -> Iterable[str]:
    prompt = get_ask_prompt(
        message=args.message,
        stack_trace=args.stack_trace,
        local_vars=args.local_vars,
        global_vars=args.global_vars,
        exception=args.exception,
    )
    return prompt_streaming(prompt)


class ExplainArgs(BaseModel):
    stack_trace: list[traceback.FrameSummary]
    local_vars: dict[str, str]
    global_vars: dict[str, str]
    exception: str = ""

    class Config:
        arbitrary_types_allowed = True


def explain(args: ExplainArgs) -> Iterable[str]:
    prompt = get_explain_prompt(
        stack_trace=args.stack_trace,
        local_vars=args.local_vars,
        global_vars=args.global_vars,
        exception=args.exception,
    )
    return prompt_streaming(prompt)
