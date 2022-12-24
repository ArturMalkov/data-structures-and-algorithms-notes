"""
BigO Notation.

Asymptotic analysis - a mathematical term used in Computer Science to try to understand the behavior of code as the
problem size gets larger and larger - what is the response?

Industry standard for quantifiable measure of how efficient certain data structures are at different tasks:
- accessing elements;
- searching for an element;
- inserting an element;
- deleting an element.

Characterizes time and space complexity of a method.
Always use the worst-case scenario.

Time complexity - equation works by inserting the size of the data-set as an integer 'n' and returns the number of operations
that need to be conducted:
- time for a method to complete;
- calculates time as function t(n) relating the number of steps given aggregate size, n.

Space complexity:
- amount of computer storage required;
- determines required space s(n) in similar fashion.

Space vs Time tradeoff:
- often you can increase performance of a method by increasing extra storage;
- extra O(1) storage is usually a good idea;
- requiring O(n) storage must be convincing.

Simplicity of code vs performance tradeoff:
- it's often easier to write code using lists but performance might suffer;
- tree-like structures are more efficient but the resulting code can be more complicated.

Asymptotic Growth:
- evaluate t(n) as problem size n doubles:
a) the true measure for understanding performance;
b) goal is to determine order of growth or O(f(n))


"Decent"/efficient complexities
- O(1) - constant - no matter the size of the data set, it'll always take the same number of instructions to run.
- O(log n) - logarithmic - gets more efficient as the size of the data set increases (e.g. binary search).
- O(n) - linear

Relatively bad complexity
- O(n log n) - slope increases as the volume of data does (unlike with O(log n)).

Inefficient complexities - the larger the data set, the more inefficient it will become.
- O(n^2) - quadratic
- O(2^n) - exponential

Worst complexity
- O(n!) - factorial
"""