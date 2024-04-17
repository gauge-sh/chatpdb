from typing import Any


def serialize_vars(vars: dict[str, Any]) -> dict[str, str]:
    return {k: str(v) for k, v in vars.items()}
