"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def iterative_str_len(a_str):
    result = 0
    for i in range(len(a_str)):
        result += 1
    return result


def recursive_str_len(a_str):
    if len(a_str) == 0:  # if a_str == ""
        # Base case
        return 0
    # Recursive case
    return 1 + recursive_str_len(a_str[1:])


input_str = "I love recursion"
print(len(input_str))  # Standard Pythonic way
print(iterative_str_len(input_str))
print(recursive_str_len(input_str))
