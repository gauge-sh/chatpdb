from types import FrameType
from typing import Optional

from chatpdb.frame import FrameData
from chatpdb.chat import AskArgs, ExplainArgs
from chatpdb.parsing.vars import serialize_vars


def parse_ask_args_from_frame(
    frame: FrameType,
    message: str,
    exception_type: Optional[type] = None,
    exception_value: str = "",
) -> AskArgs:
    frame_data = FrameData.from_frame(frame=frame)
    if exception_type and exception_value:
        exception = f"{exception_type.__name__}: {exception_value}"
    else:
        exception = ""
    return AskArgs(
        message=message,
        source_code=frame_data.source_code,
        stack_trace=frame_data.stack_trace,
        local_vars=serialize_vars(frame_data.locals_dict),
        global_vars=serialize_vars(frame_data.globals_dict),
        exception=exception,
    )


def parse_explain_args_from_frame(
    frame: FrameType, exception_type: Optional[type] = None, exception_value: str = ""
) -> ExplainArgs:
    frame_data = FrameData.from_frame(frame=frame)
    if exception_type and exception_value:
        exception = f"{exception_type.__name__}: {exception_value}"
    else:
        exception = ""
    return ExplainArgs(
        source_code=frame_data.source_code,
        stack_trace=frame_data.stack_trace,
        local_vars=serialize_vars(frame_data.locals_dict),
        global_vars=serialize_vars(frame_data.globals_dict),
        exception=exception,
    )
