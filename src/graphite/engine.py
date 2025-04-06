from graphite.node import Node
from graphite.states import ExecutionState
from typing import List, Dict, Any, Callable, Optional
from threading import Event
import logging


class Engine:
    def __init__(self, name: str):
        self.name = name
        self.nodes: List[Node] = []
        self.subsystems: Dict[str, Dict[str, Any]] = {}
        self.running: bool = False

    def add_logger(self, logger: logging.Logger = None) -> None:
        if logger is None:
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(self.name)
        else:
            self.logger = logger

    def add_node(
        self,
        node_func: Callable,
        inputs: Optional[List[Node]] = None,
        name: Optional[str] = None,
    ) -> Node:
        node_name = name if name else node_func.__name__
        node = Node(func=node_func, name=node_name, inputs=inputs or [])
        self.nodes.append(node)
        return node

    def run(self, stop_event: Event = Event()):
        self.stop_event = stop_event
        try:
            self._run_loop()
        except Exception as e:
            print(f"Error in processing loop: {str(e)}")

    def stop(self):
        self.stop_event.set()

    def _run_loop(self):

        while not self.stop_event.is_set():
            node_index = 0

            while node_index < len(self.nodes):
                node = self.nodes[node_index]

                input_values = self._get_input_values(node)
                func_output, node_status, execution_state = node.func(*input_values)

                if execution_state == ExecutionState.TERMINATE:
                    self.stop_event.set()
                    break

                if execution_state == ExecutionState.RETURN:
                    for n in self.nodes:
                        n.output = None
                        node_index = 0  # Go back to the first task
                        continue

                if execution_state == ExecutionState.FORWARD:
                    node_index += 1

                if execution_state not in ExecutionState:
                    raise ValueError("Not valid ExecutionState.")

    def _get_input_values(self, node: Node) -> List[Any]:
        input_values = []
        for input_node in node.inputs:
            input_values.append(input_node.output)

        return input_values
