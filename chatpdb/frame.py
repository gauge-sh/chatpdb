import inspect
import traceback
from types import FrameType
from typing import Any
from rich.console import Console

from pydantic import BaseModel


class FrameData(BaseModel):
    frame: FrameType
    source_code: str
    locals_dict: dict[str, Any]
    globals_dict: dict[str, Any]
    stack_trace: list[traceback.FrameSummary]

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def from_frame(cls, frame: FrameType) -> "FrameData":
        source_code = inspect.getsource(frame)
        locals_dict = frame.f_locals
        globals_dict = frame.f_globals
        stack_trace = traceback.extract_stack(frame)
        return cls(
            frame=frame,
            source_code=source_code,
            locals_dict=locals_dict,
            globals_dict=globals_dict,
            stack_trace=stack_trace,
        )


def hook(frame: FrameType):
    frame_data = FrameData.from_frame(frame)

    console = Console()
    console.print(frame_data)

    # yield []
