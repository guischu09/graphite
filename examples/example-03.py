import sys
import os

graphite_path = os.path.join(os.getcwd(), "src")
sys.path.append(os.path.abspath(graphite_path))

from graphite.node import NodeStatus
from graphite.states import ExecutionState
from graphite.engine import Engine
import random

# Track execution
exec_count = 0


def task_a():
    global exec_count
    exec_count += 1
    print(f"Executing Task A (run #{exec_count})")
    return "Result A", NodeStatus.SUCCESS, ExecutionState.FORWARD


def task_b(a_result):
    print(f"Executing Task B with input: {a_result}")
    return "Result B", NodeStatus.SUCCESS, ExecutionState.FORWARD


def check_b(b_result):
    """Check if B result meets criteria"""
    print(f"Checking B result: {b_result}")
    random_value = random.random()
    print(f"Random value: {random_value}")

    if 0.5 > random_value:
        print("B check passed, FORWARDing to C...")
        return True, NodeStatus.SUCCESS, ExecutionState.FORWARD
    else:
        print("B check failed, returning to the beginning...")
        return False, NodeStatus.SUCCESS, ExecutionState.RETURN


def task_c(check_b_result):
    print(f"Executing Task C with input: {check_b_result}")
    return "Result C", NodeStatus.SUCCESS, ExecutionState.FORWARD


def check_c(c_result):
    """Check if C result meets criteria"""
    print(f"Checking C result: {c_result}")
    random_value = random.random()
    print(f"Random value: {random_value}")

    if 0.5 > random_value:
        print("C check passed, FORWARDing to D...")
        return True, NodeStatus.SUCCESS, ExecutionState.FORWARD
    else:
        print("C check failed, returning to the beginning...")
        return False, NodeStatus.SUCCESS, ExecutionState.RETURN


def task_d(check_c_result):
    print(f"Executing Task D with input: {check_c_result}")
    return "Result D", NodeStatus.SUCCESS, ExecutionState.FORWARD


def check_d(d_result):
    """Check if D result meets criteria"""
    print(f"Checking D result: {d_result}")
    random_value = random.random()
    print(f"Random value: {random_value}")

    if 0.5 > random_value:
        print("D check passed, FORWARDing to E...")
        return True, NodeStatus.SUCCESS, ExecutionState.FORWARD
    else:
        print("D check failed, returning to the beginning...")
        return False, NodeStatus.SUCCESS, ExecutionState.RETURN


def task_e(check_d_result):
    print(f"Executing Task E with input: {check_d_result}")
    return "Result E", NodeStatus.SUCCESS, ExecutionState.FORWARD


def check_e(e_result):
    """Check if E result meets criteria"""
    print(f"Checking E result: {e_result}")
    random_value = random.random()
    print(f"Random value: {random_value}")

    if 0.5 > random_value:
        print("E check passed, FORWARDing to Exit...")
        return True, NodeStatus.SUCCESS, ExecutionState.FORWARD
    else:
        print("E check failed, returning to the beginning...")
        return False, NodeStatus.SUCCESS, ExecutionState.RETURN


def exit_task(check_e_result):
    print(f"Exiting with result: {check_e_result}")
    return None, NodeStatus.SUCCESS, ExecutionState.TERMINATE


# Set up the engine
engine = Engine("condition_flow_engine")

# Task A (starting point)
task_a = engine.add_node(task_a, name="A")

# Task B and its check
task_b = engine.add_node(task_b, inputs=[task_a], name="B")
check_b = engine.add_node(check_b, inputs=[task_b], name="Check B")

# Task C and its check
task_c = engine.add_node(task_c, inputs=[check_b], name="C")
check_c = engine.add_node(check_c, inputs=[task_c], name="Check C")

# Task D and its check
task_d = engine.add_node(task_d, inputs=[check_c], name="D")
check_d = engine.add_node(check_d, inputs=[task_d], name="Check D")

# Task E and its check
task_e = engine.add_node(task_e, inputs=[check_d], name="E")
check_e = engine.add_node(check_e, inputs=[task_e], name="Check E")

# Exit task
exit_task = engine.add_node(exit_task, inputs=[check_e], name="Exit")

# Set a maximum number of iterations to avoid potentially infinite loops
max_iterations = 10000000000
exec_count = 0

# Start the engine
print("\nStarting engine with a maximum of", max_iterations, "iterations")
print("Each check has a 50% chance of passing\n")

# Seed random for reproducibility in this example
random.seed(42)

# Start the engine
engine.run()
print("\nengine has terminated")
print(f"Total executions of task A: {exec_count}")
