from types import FrameType

from chatpdb.frame import FrameData
from chatpdb.chat import AskArgs, ExplainArgs


def parse_ask_args_from_frame(frame: FrameType, message: str) -> AskArgs:
    frame_data = FrameData.from_frame(frame=frame)
    return AskArgs(
        message=message,
        source_code=frame_data.source_code,
        stack_trace=list(map(str, frame_data.stack_trace)),
        local_vars={},
        global_vars={}
        # local_vars=json.loads(json.dumps(frame_data.locals_dict)),
        # global_vars=json.loads(json.dumps(frame_data.globals_dict)),
    )


def parse_explain_args_from_frame(frame: FrameType) -> ExplainArgs:
    frame_data = FrameData.from_frame(frame=frame)
    return ExplainArgs(
        source_code=frame_data.source_code,
        stack_trace=list(map(str, frame_data.stack_trace)),
        local_vars={},
        global_vars={}
        # local_vars=json.loads(json.dumps(frame_data.locals_dict)),
        # global_vars=json.loads(json.dumps(frame_data.globals_dict)),
    )
