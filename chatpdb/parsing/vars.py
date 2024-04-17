from typing import Any, Dict


def serialize_vars(vars: Dict[str, Any]) -> Dict[str, str]:
    return {k: str(v) for k, v in vars.items()}
