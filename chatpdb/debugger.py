import sys
from types import FrameType
from typing import Optional

from IPython.terminal.debugger import TerminalPdb
from IPython.core.debugger import Pdb

from rich.console import Console

from chatpdb.chat import ask, explain
from chatpdb.parsing import parse_ask_args_from_frame, parse_explain_args_from_frame

console = Console()


def handle_chat_pdb(frame: Optional[FrameType], arg: str):
    if not frame:
        console.print("ChatPDB: No frame available")
        return
    # Will be None, None, None if no exception
    exception_type, exception_value, _ = sys.exc_info()
    if arg:
        ask_args = parse_ask_args_from_frame(
            frame,
            message=arg,
            exception_type=exception_type,
            exception_value=exception_value,
        )
        for line in ask(ask_args):
            console.print(line, end="")
    else:
        explain_args = parse_explain_args_from_frame(
            frame,
            exception_type=exception_type,
            exception_value=exception_value,
        )
        for line in explain(explain_args):
            console.print(line, end="")

    # Newline
    console.print("")


# For use in rich IPython environments
class TerminalChatPdb(TerminalPdb):
    def do_y(self, arg: str):
        """y "prompt"

        Ask ChatGPT to explain the current code and stack trace.
        Optionally prompt for a more specific answer.
        """
        handle_chat_pdb(self.curframe, arg)  # type: ignore


# For use with simple_prompt IPython instances
class ChatPdb(Pdb):
    def do_y(self, arg: str):
        handle_chat_pdb(self.curframe, arg)
