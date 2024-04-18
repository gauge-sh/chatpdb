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
Provide a response to the message from the User below.
Use the context above to inform your response.
The context information comes from a currently running Python debugger session.

## Message from the User
{user_message}
"""
)

exception_template = (
    shared_context_template
    + """
<exception>
{exception}
</exception>

## Instructions
Provide a response to the message from the User below.
Use the context above to inform your response.
The context information comes from a currently running Python debugger session.
This includes an exception that has just been raised, which is likely
 what the User is interested in, unless they indicate otherwise.
 
 ## Message from the User
 {user_message}
 """
)


def get_ask_prompt(
    message: str,
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
            user_message=message,
            exception=exception,
        )
    return template.format(
        stack_trace=format_stack_trace(stack_trace),
        locals=format_vars(local_vars),
        globals=format_vars(global_vars),
        user_message=message,
    )
