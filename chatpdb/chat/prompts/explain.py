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
The context information comes from a currently running Python debugger session.
Use this information to explain the current state of the program, focusing specifically on the
 most relevant pieces of code, variable state, or the stack trace.
Your response must:
- be clear and concise
- focus on the most relevant information, particularly any errors, issues, or recent state changes
- make minimal assumptions about external code or context
"""


def get_explain_prompt(
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
    )
