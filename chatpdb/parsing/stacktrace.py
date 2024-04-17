import traceback


def serialize_stacktrace(stacktrace: list[traceback.FrameSummary]) -> list[str]:
    return list(map(str, stacktrace))
