from typing import Iterable

from pydantic import BaseModel
from chatpdb.chat.prompts import get_ask_prompt, get_explain_prompt
from chatpdb.chat.llm import prompt_streaming


class AskArgs(BaseModel):
    message: str
    source_code: str
    stack_trace: list[str]
    local_vars: dict[str, str]
    global_vars: dict[str, str]


def ask(args: AskArgs) -> Iterable[str]:
    prompt = get_ask_prompt(
        message=args.message,
        stack_trace=args.stack_trace,
        source_code=args.source_code,
        local_vars=args.local_vars,
        global_vars=args.global_vars,
    )
    return prompt_streaming(prompt)


class ExplainArgs(BaseModel):
    source_code: str
    stack_trace: list[str]
    local_vars: dict[str, str]
    global_vars: dict[str, str]


def explain(args: ExplainArgs) -> Iterable[str]:
    prompt = get_explain_prompt(
        stack_trace=args.stack_trace,
        source_code=args.source_code,
        local_vars=args.local_vars,
        global_vars=args.global_vars,
    )
    return prompt_streaming(prompt)
