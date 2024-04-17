import traceback
from typing import List


def serialize_stacktrace(stacktrace: List[traceback.FrameSummary]) -> List[str]:
    return list(map(str, stacktrace))
