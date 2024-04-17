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

    if arg:
        ask_args = parse_ask_args_from_frame(frame, message=arg)
        for line in ask(ask_args):
            console.print(line, end="")
    else:
        explain_args = parse_explain_args_from_frame(frame)
        for line in explain(explain_args):
            console.print(line, end="")

    # Newline
    console.print()


# For use outside a shell environment
class ChatPdb(Pdb):
    def do_x(self, arg: str):
        handle_chat_pdb(self.curframe, arg=arg)


# For use inside shell environments
class TerminalChatPdb(TerminalPdb):
    def do_x(self, arg: str):
        handle_chat_pdb(self.curframe, arg=arg)
