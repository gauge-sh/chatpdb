from IPython.terminal.debugger import TerminalPdb
from rich.console import Console

from chatpdb.frame import hook

console = Console()


class ChatPdb(TerminalPdb):
    def do_y(self, arg):
        hook(self.curframe)
