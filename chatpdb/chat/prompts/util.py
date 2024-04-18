import os
import sys
import site
import traceback
from typing import Optional, List, Dict

from rich.console import Console

console = Console()


def format_stack_trace(stack_trace: List[traceback.FrameSummary]) -> str:
    file_contents = {}
    exclude_paths = [sys.base_prefix, sys.prefix] + site.getsitepackages()

    for frame in stack_trace:
        filename = frame.filename
        full_path = os.path.abspath(filename)
        if not any(
            full_path.startswith(os.path.abspath(ex_path)) for ex_path in exclude_paths
        ):
            try:
                with open(full_path, "r") as file:
                    # Format with line numbers
                    content = []
                    for i, line in enumerate(file.readlines()):
                        if i + 1 == frame.lineno:
                            content.append(f"> {i + 1} | {line}")
                        else:
                            content.append(f"  {i + 1} | {line}")
                    file_contents[filename] = "".join(content)
            except (FileNotFoundError, IOError):
                # Just continue if we can't read the file
                # Later we can show a warning in verbose mode or similar
                pass

    files = []
    for frame in stack_trace:
        if frame.filename not in file_contents:
            files.append(
                f"<file\nname='{frame.filename}'\nscope='{frame.name}'>\n(3rd party code)\n</file>"
            )
        else:
            files.append(
                f"<file\nname='{frame.filename}'\nscope='{frame.name}'\nline={frame.lineno}>\n"
                f"<content>\n{file_contents[frame.filename]}\n</content>\n"
                "</file>"
            )
    return "\n".join(files)


def format_vars(
    vars_dict: Dict[str, str], exclude_list: Optional[List[str]] = None
) -> str:
    exclude_list = exclude_list or [
        "__builtins__",
        "__loader__",
        "__doc__",
        "__package__",
        "__spec__",
        "__file__",
        "__cached__",
    ]
    return "\n".join(f"{k}: {v}" for k, v in vars_dict.items() if k not in exclude_list)
