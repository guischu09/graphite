# graphite

**Graph Iterative Task Engine**

graphite is a lightweight framework for building and executing computational graphs with state machine characteristics. It allows you to define a series of interconnected processing nodes and control the flow of execution between them.

## Features

- **Directed Graph Execution**: Define dependencies between processing nodes
- **State Machine Flow Control**: Control execution flow with states like CONTINUE, TERMINATE, PAUSE, and RETURN
- **Simple API**: Easy-to-use interface for creating and connecting nodes


## Quick Start

```python
from graphite.engine import Engine
from graphite.node import NodeStatus
from graphite.states import ExecutionState

# Create a new engine
engine = Engine(name="my_processor")

# Add logging
engine.add_logger()

# Define some processing functions
def data_source():
    data = {"value": 42}
    return data, NodeStatus.SUCCESS, ExecutionState.CONTINUE

def process_data(input_data):
    result = input_data["value"] * 2
    return result, NodeStatus.SUCCESS, ExecutionState.CONTINUE

def output_result(result):
    print(f"Final result: {result}")
    return None, NodeStatus.SUCCESS, ExecutionState.TERMINATE

# Add nodes to the engine
source_node = engine.add_node(data_source)
process_node = engine.add_node(process_data, inputs=[source_node])
output_node = engine.add_node(output_result, inputs=[process_node])

# Run the engine
engine.run()
```

## Execution States

| State | Description |
|-------|-------------|
| CONTINUE | Proceed to the next node in the graph |
| TERMINATE | Stop all execution of the engine |
| PAUSE | Temporarily pause execution (can be resumed) |
| RETURN | Reset outputs and restart from the beginning |


## License

This project is licensed under the MIT License - see the LICENSE file for details.