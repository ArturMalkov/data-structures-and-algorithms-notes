class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_node(head, data):
    # base case - if we hit null, then we've recursed to our end goal according to BST property (insertions always happen at the leaf level)
    # insertions always happen at the end - if we've done all the comparisons till the very end, then we've hit the valid position
    if head is None:
        head = Node(data)
        return head

    # if data is greater than the node, then we need to recurse to the right
    if head.data < data:
        head.right = insert_node(head.right, data)
    # if data is smaller then the node, then we need to recurse to the left
    else:
        head.left = insert_node(head.left, data)
    # return the original node of the tree
    return head
