from typing import List, Dict
import traceback

from chatpdb.chat.prompts.util import format_stack_trace, format_vars

shared_context_template = """
## Context
<stacktrace>
{stack_trace}
</stacktrace>
<frame_variables>
<locals>
{locals}
</locals>
<globals>
{globals}
</globals>
</frame_variables>
"""

template = (
    shared_context_template
    + """
## Instructions
The context information comes from a currently running Python debugger session.
Use this information to explain the current state of the program, focusing specifically on the
 most relevant pieces of code, variable state, or the stack trace.
Your response must:
- be clear and concise
- focus on the most relevant information, particularly any errors, issues, or recent state changes
- make minimal assumptions about external code or context
"""
)

exception_template = (
    shared_context_template
    + """
<exception>
{exception}
</exception>

## Instructions
The context information comes from a currently running Python debugger session.
The context includes an exception that was just raised.
Explain why the exception occurred and how it relates to the current state of the program.

Your response must:
- be clear and concise
- focus on the most relevant information
- make minimal assumptions about external code or context
"""
)


def get_explain_prompt(
    stack_trace: List[traceback.FrameSummary],
    local_vars: Dict[str, str],
    global_vars: Dict[str, str],
    exception: str = "",
) -> str:
    if exception:
        return exception_template.format(
            stack_trace=format_stack_trace(stack_trace),
            locals=format_vars(local_vars),
            globals=format_vars(global_vars),
            exception=exception,
        )
    return template.format(
        stack_trace=format_stack_trace(stack_trace),
        locals=format_vars(local_vars),
        globals=format_vars(global_vars),
    )
