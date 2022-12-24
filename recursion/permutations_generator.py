"""
{1, 2, 3, ..., N} - numbers

N N-1 N-2    2  1   = N! (combinatorics in action)
__ __ __ ... __ __
"""


def generate_number(N: int, M: int, prefix=None):
    """Generates all permutations of a list with length M and numbers in range from 0 to N"""
    prefix = prefix or []  # will create [] if prefix is None (even though [] is evaluated to False)
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()


generate_number(3, 3)


def simplest_perm_generator(M, prefix=""):
    if M == 0:
        print(prefix)
    # else:
    #     simplest_perm_generator(M-1, prefix+"0")
    #     simplest_perm_generator(M-1, prefix+"1")
    for digit in "0", "1":  # for binary system
        simplest_perm_generator(M-1, prefix+digit)


simplest_perm_generator(3)

#
#
# print(prefix) - "00"
# simplest_perm_generator(1, "00")
# simplest_perm_generator(2, "0")


def generate_permutations(N: int, M: int=-1, prefix=None):
    """Generates all permutations for N digits in M positions with prefix"""
    M = N if M == -1 else M  # by default, N figures in N positions
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        