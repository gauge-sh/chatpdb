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
    error_class, error_name, _ = sys.exc_info()
    print(error_class, error_name)
    if arg:
        ask_args = parse_ask_args_from_frame(frame, message=arg)
        for line in ask(ask_args):
            console.print(line, end="")
    else:
        explain_args = parse_explain_args_from_frame(frame)
        for line in explain(explain_args):
            console.print(line, end="")

    # Newline
    console.print("")


class ChatPdbMixin:
    def do_y(self, arg: str):
        """y "prompt"

        Ask ChatGPT to explain the current code and stack trace.
        Optionally prompt for a more specific answer.
        """
        handle_chat_pdb(self.curframe, arg)  # type: ignore


# For use in rich IPython environments
class TerminalChatPdb(ChatPdbMixin, TerminalPdb): ...


# For use with simple_prompt IPython instances
class ChatPdb(ChatPdbMixin, Pdb): ...
