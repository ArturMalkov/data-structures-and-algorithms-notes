def string_reversal(some_string):
    # Base case
    if len(some_string) == 0:  # when can I no longer continue?
        return ""
    # Between each invocation, what's the smallest unit I can reverse to contribute to the goal?
    # shrinks the problem space                 smallest unit of work to contribute
    return some_string[len(some_string)-1] + string_reversal(some_string[:len(some_string)-1])
    # or
    # return string_reversal(some_string[1:]) + some_string[0]
    # shrinks the problem space                 smallest unit of work to contribute


print(string_reversal("Hello, world!"))
