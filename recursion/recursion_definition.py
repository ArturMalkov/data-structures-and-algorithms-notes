"""
Recursion - a function that calls itself... until it doesn't.

Call stack - stores functions' invocations within our program.
Call stack allows us to understand what memory addresses we return our data to and stores local namespaces (arguments passed, etc.)
Call stack is filled with stack frames. Stack frame of a particular function is popped from the call stack as soon as it finishes executing (not earlier!).

Recursion depth (number of calls) - limit is 1000
Stack overflow - exceeding the volume of call stack (due to the number of recursive calls)
Base case and recursive case must be implemented to each case
subtask (to be solved by further recursive call) has to be easier than the task (task from previous recursive call)
(i.e. closer to base case)

Recursive case - how are we going to solve the task by diminishing the difficulty of the original task via subtasks of lesser difficulty step-by-step
Recursion must:
- have a base case - which returns(!) (some value) (stopping condition - no longer grow the number of recursive calls in memory (thus, it has to be true at some point))
- change its state and move towards its base case (each invocation further gets you closer to the problem you're trying to solve, i.e. makes a problem smaller)
- have a recursive case

Stages of a recursive algorithm:
1) Winding - what happens before we hit the base case:
When a function is called in Python, stack frame is allocated to store the local variables for that function.
Each recursive call adds a stack frame to the call stack until we reach the base case - winding.
2) Unwinding - what happens after we hit the base case:
Once the base case is reached (turnaround point), the stack begins to unwind as each call returns its results (each subsequent call is popped of the call stack).
Remember ATM analogy!
Values from recursive calls on the top of the call stack are returned to the stack frames that preceeded those recursive calls
Result propagates itself downwards through the stack frames to the initial call.
"""


def matryoshka(n):  # n - number of nested matryoshkas
    if n == 1:  # base case
        print("Matryoshka")  # result from the very top of the call stack - top-down direction
    else:
        print(f"Upper part of matryoshka {n=}")  # on the way to the base case (up the call stack)
        matryoshka(n-1)  # recursive case
        print(f"Lower part of matryoshka {n=}")  # on the way back (down the call stack)


matryoshka(4)


# FACTORIAL
# n! = (n-1)! * n

def factorial(n):
    assert n >= 0, "Factorial of negative numbers is not defined"
    if n == 0:
        return 1
    return factorial(n-1) * n

# call stack
# factorial(4):
#
# factorial(0) * 1  # 1*1 = 1
# ^^^
# factorial(1) * 2  # 1*2 = 2
# ^^^
# factorial(2) * 3  # 2*3=6
# ^^^
# factorial(3) * 4  # 6*4 = 24
