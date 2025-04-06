from typing import Callable
from graphite.states import ExecutionState


def exec_forward(node_func: Callable):
    def set_forward_node(*args, **kargs):
        result = node_func(*args, **kargs)
        if isinstance(result, tuple) and len(result) == 2:
            return (*result, ExecutionState.FORWARD)
        else:
            raise ValueError(
                f"Function {node_func.__name__} must return (output, status)"
            )

    return set_forward_node


def exec_pause(node_func: Callable):
    def set_pause_node(*args, **kargs):
        result = node_func(*args, **kargs)
        if isinstance(result, tuple) and len(result) == 2:
            return (*result, ExecutionState.PAUSE)
        else:
            raise ValueError(
                f"Function {node_func.__name__} must return (output, status)"
            )

    return set_pause_node


def exec_return(node_func: Callable):
    def set_return_node(*args, **kargs):
        result = node_func(*args, **kargs)
        if isinstance(result, tuple) and len(result) == 2:
            return (*result, ExecutionState.RETURN)
        else:
            raise ValueError(
                f"Function {node_func.__name__} must return (output, status)"
            )

    return set_return_node


def exec_terminate(node_func: Callable):
    def set_terminate_node(*args, **kargs):
        result = node_func(*args, **kargs)
        if isinstance(result, tuple) and len(result) == 2:
            return (*result, ExecutionState.TERMINATE)
        else:
            raise ValueError(
                f"Function {node_func.__name__} must return (output, status)"
            )

    return set_terminate_node
