import sys

from IPython.terminal.debugger import TerminalPdb
from IPython.core.debugger import Pdb

from rich.console import Console

from chatpdb.frame import hook

console = Console()


class ChatPdbMixin:
    def do_y(self, arg: str):
        if self.curframe:
            error_class, error_name, _ = sys.exc_info()
            hook(self.curframe, arg, error_name, error_class)
        else:
            raise ValueError("Unable to access current frame.")


# For use with simple_prompt IPython instances
class ChatPdb(ChatPdbMixin, Pdb): ...


# For use in rich IPython environments
class TerminalChatPdb(ChatPdbMixin, TerminalPdb): ...
