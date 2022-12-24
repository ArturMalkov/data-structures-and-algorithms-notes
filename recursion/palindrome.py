def is_palindrome(some_string):
    # Base case / stopping condition
    if len(some_string) <= 1:
        return True
    # Recursive case - do some work to shrink the problem space
    if some_string[0] == some_string[len(some_string)-1]:
        return is_palindrome(some_string[1:len(some_string)-1])

    # Additional base case to handle non-palindromes
    return False


print(is_palindrome("kayak"))
