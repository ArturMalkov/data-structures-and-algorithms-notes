"""
Memory considerations:
- When recursion is called, frames containing data for each successive call are added to the stack
- Python has a limit for recursive calls to avoid using up too much memory
otherwise - RecursionError: maximum recursion depth exceeded

Solution - reset default recursion limit to a new value
See "recursion_limit" file.
"""

import sys


print(sys.getrecursionlimit())  # 1000 is default
sys.setrecursionlimit(1002)  # sets a custom value for recursion depth
