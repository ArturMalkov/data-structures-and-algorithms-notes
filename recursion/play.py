# step by step
def search(lst, target):
    for elem in lst:
        if elem == target:
            return True
    return False


# recursive code
def search_recursive(lst, target):
    if len(lst) == 0:
        return False

    if lst[0] == target:
        return True
    return search_recursive(lst[1:], target)


class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def search(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    return search(node.next, value)


def sum_list(node):
    if node is None:
        return 0
    return node.value + sum_list(node.next)
