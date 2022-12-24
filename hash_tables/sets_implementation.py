"""
Implementation steps:
1) design a function that returns a relatively small number for each element passed in (hash function)
(e.g. f(x) = x % 10);
2) calculate the result of the hash function;
3) put element to a list with an index equal to the number returned from the hash function.

Since hash_function(137) = hash_function(17), collisions are possible.
(Collisions occur when results of a hash function are the same for different arguments).
Results of the hash function need to be evenly distributed to avoid too frequent collisions.
"""


set_size = 10
my_set = [[] for _ in range(set_size)]  # hash table


def add(value):
    if not find(value):
        my_set[value % set_size].append(value)  # value % set_size - hash function


def find(value):
    for element in my_set[value % set_size]:
        if element == value:
            return True
    return False


def delete(value):
    target_list = my_set[value % set_size]
    for i in range(len(target_list)):
        if target_list[i] == value:
            target_list[i], target_list[len(target_list) - 1] = target_list[len(target_list) - 1], target_list[i]
            target_list.pop()
            return
