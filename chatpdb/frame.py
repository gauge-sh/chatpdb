import inspect
import traceback
from types import FrameType
from typing import Any, Optional, Type, List, Dict
from rich.console import Console

from pydantic import BaseModel


class FrameData(BaseModel):
    frame: FrameType
    source_code: str
    locals_dict: Dict[str, Any]
    globals_dict: Dict[str, Any]
    stack_trace: List[traceback.FrameSummary]

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def from_frame(cls, frame: FrameType) -> "FrameData":
        try:
            source_code = inspect.getsource(frame)
        except OSError:
            source_code = "Source code not available, likely running in a REPL or interactive environment."
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


def hook(
    frame: FrameType,
    prompt: Optional[str] = None,
    error_name: Optional[str] = None,
    error_class: Optional[Type[BaseException]] = None,
):
    frame_data = FrameData.from_frame(frame)

    console = Console()
    console.print(frame_data)
    console.print("PROMPT:", prompt)
    console.print("ERROR NAME:", error_name)
    console.print("ERROR CLASS:", error_class)
    # yield []
