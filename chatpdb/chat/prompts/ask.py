template = """
## Context
<stacktrace>
{stack_trace}
</stacktrace>
<code>
{source_code}
</code>
<frame_variables>
<locals>
{locals}
</locals>
<globals>
{globals}
</globals>
</frame_variables>

## Instructions
Provide a response to the message from the User below.
Use the context above to inform your response.
The context information comes from a currently running Python debugger session.

## Message from the User
{user_message}
"""


def get_ask_prompt(
    message: str,
    stack_trace: list[str],
    source_code: str,
    local_vars: dict[str, str],
    global_vars: dict[str, str],
) -> str:
    return template.format(
        stack_trace="\n".join(stack_trace),
        source_code=source_code,
        locals="\n".join(f"{k}: {v}" for k, v in local_vars.items()),
        globals="\n".join(f"{k}: {v}" for k, v in global_vars.items()),
        user_message=message,
    )
