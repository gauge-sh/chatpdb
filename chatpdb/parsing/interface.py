from types import FrameType

from chatpdb.frame import FrameData
from chatpdb.chat import AskArgs, ExplainArgs
from chatpdb.parsing.stacktrace import serialize_stacktrace
from chatpdb.parsing.vars import serialize_vars


def parse_ask_args_from_frame(frame: FrameType, message: str) -> AskArgs:
    frame_data = FrameData.from_frame(frame=frame)
    return AskArgs(
        message=message,
        source_code=frame_data.source_code,
        stack_trace=serialize_stacktrace(frame_data.stack_trace),
        local_vars=serialize_vars(frame_data.locals_dict),
        global_vars=serialize_vars(frame_data.globals_dict),
    )


def parse_explain_args_from_frame(frame: FrameType) -> ExplainArgs:
    frame_data = FrameData.from_frame(frame=frame)
    return ExplainArgs(
        source_code=frame_data.source_code,
        stack_trace=serialize_stacktrace(frame_data.stack_trace),
        local_vars=serialize_vars(frame_data.locals_dict),
        global_vars=serialize_vars(frame_data.globals_dict),
    )
