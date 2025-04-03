from enum import Enum


class ExecutionState(str, Enum):
    CONTINUE: str = "CONTINUE"
    TERMINATE: str = "TERMINATE"
    PAUSE: str = "PAUSE"
    RETURN: str = "RETURN"
