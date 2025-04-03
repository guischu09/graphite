from graphite.engine import Engine
from graphite.states import ExecutionState
from graphite.node import NodeStatus
from threading import Event


def hello_world() -> None:
    print_statement = "Hello World"
    print(print_statement)
    return print_statement, NodeStatus.SUCCESS, ExecutionState.CONTINUE


def stop_hello_world(world_output) -> None:
    print(f"Stopping after: {world_output}")
    return None, NodeStatus.SUCCESS, ExecutionState.TERMINATE


def main():

    engine = Engine("hello_world")
    output = engine.add_node(hello_world)
    engine.add_node(stop_hello_world, inputs=[output])

    engine.run(stop_event=Event())


if __name__ == "__main__":
    main()
