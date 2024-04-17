from pydantic import BaseModel


class AskArgs(BaseModel):
    question: str
    source_code: str
    stack_trace: list[str]
    stack_frame_context: dict[str, str]


def ask(args: AskArgs): ...


class ExplainArgs(BaseModel):
    source_code: str
    stack_trace: list[str]
    stack_frame_context: dict[str, str]


def explain(args: ExplainArgs): ...
