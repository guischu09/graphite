import sys
import os

graphite_path = os.path.join(os.getcwd(), "src")
sys.path.append(os.path.abspath(graphite_path))

from graphite.engine import Engine
from graphite.node import NodeStatus
from graphite.sugar import exec_forward, exec_terminate
from threading import Event


@exec_forward
def hello_world() -> None:
    print_statement = "Hello World"
    print(print_statement)
    return (
        print_statement,
        NodeStatus.SUCCESS,
    )


@exec_terminate
def stop_hello_world(world_output) -> None:
    print(f"Stopping after: {world_output}")
    return None, NodeStatus.SUCCESS


def main():

    engine = Engine("hello_world")
    output = engine.add_node(node_func=hello_world)
    engine.add_node(stop_hello_world, inputs=[output])

    engine.run(stop_event=Event())


if __name__ == "__main__":
    main()
