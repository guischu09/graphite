from enum import Enum
from dataclasses import dataclass, field
from typing import Callable, Any


class NodeStatus(str, Enum):
    SUCCESS: str = "SUCCESS"
    ERROR: str = "ERROR"
    NULL: str = "NULL"


@dataclass
class Node:
    name: str
    func: Callable
    inputs: list["Node"] = field(default_factory=list)
    output: Any = None

    def __hash__(self):
        return hash((id(self.func), self.name))

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return id(self.func) == id(other.func) and self.name == other.name
