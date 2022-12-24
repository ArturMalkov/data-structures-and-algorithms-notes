"""
Tail Call Optimization - compiler optimization in certain languages to reduce stack overflows (via optimizing the number of stack frames):
- executes recursive function calls in the current stack frame and returns results (rather than creating a new stack frame),
thus allowing to save a lot of memory;
- this works by enrsuring the last function call is a recursive one ("n * factorial(n-1)" is not tail recursive -
the return value is not just a recursive call - instead use "return factorial(n-1, n*multiplier)");
- Python doesn't have this feature (neither does Java)!!!

When the only thing returned from a function is a recursive call, it is known as tail recursion.
See "tail_recursion" file.
"""
