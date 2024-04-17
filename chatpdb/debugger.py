import inspect
import sys
import traceback

from IPython.terminal.debugger import TerminalPdb
from rich.console import Console

console = Console()


class ChatPdb(TerminalPdb):
    def do_y(self, arg):
        locals_dict = self.curframe.f_locals
        stack = traceback.extract_stack(self.curframe)
        showcase(locals_dict, inspect.getsource(self.curframe), stack)


def showcase(locals_dict: dict, source: str, frame_summaries: list[traceback.FrameSummary]) -> None:
    console.print("LOCALS_DICT:", locals_dict)
    console.print("SOURCE:", source)
    console.print("TRACEBACK:", frame_summaries)
