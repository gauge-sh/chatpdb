from IPython.terminal.debugger import TerminalPdb
from IPython.core.debugger import Pdb

from rich.console import Console

from chatpdb.frame import hook

console = Console()


# For use outside of a shell environment
class ChatPdb(Pdb):
    def do_x(self, arg: str):
        # TODO print output
        hook(self.curframe, arg)


# For use inside shell environments
class TerminalChatPdb(TerminalPdb):
    def do_x(self, arg: str):
        # TODO print output
        hook(self.curframe, arg)
