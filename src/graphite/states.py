from enum import Enum


class ExecutionState(str, Enum):
    FORWARD: str = "FORWARD"
    TERMINATE: str = "TERMINATE"
    PAUSE: str = "PAUSE"
    RETURN: str = "RETURN"
