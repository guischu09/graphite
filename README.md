# graphite

**Graph Iterative Task Engine**

graphite is a declarative framework for building and executing computational graphs with state machine characteristics. It allows you to define a series of interconnected processing nodes and control the flow of execution between them.

## Features

- **Directed Graph Execution**: Define dependencies between processing nodes
- **State Machine Flow Control**: Control execution flow
- **Simple API**: Easy-to-use interface for creating and connecting nodes


## Quick Start

```python
from graphite.engine import Engine
from graphite.states import ExecutionState
from graphite.node import NodeStatus
from threading import Event


def hello_world() -> None:
    print_statement = "Hello World"
    print(print_statement)
    return print_statement, NodeStatus.SUCCESS, ExecutionState.FORWARD


def stop_hello_world(world_output) -> None:
    print(f"Stopping after: {world_output}")
    return None, NodeStatus.SUCCESS, ExecutionState.TERMINATE


engine = Engine("hello_world")
output = engine.add_node(hello_world)
engine.add_node(stop_hello_world, inputs=[output])

engine.run(stop_event=Event())
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.