"""
Traversing tree structures is one of the most important applications of recursion.
A tree is a data structure consisting of nodes connected by direct edges.
A tree consists of a root node and one or more subtrees (inherently recursive structure).

Depth-first traversals of a binary tree:
1) in-order traversal (root->left->right):
- used if you know you need to explore the roots before inspecting any leaves;
- used to create a copy of a tree.

2) pre-order traversal(left->root->right):
- visits the nodes in alphabetical order;
- used if you know that a tree has an inherent sequence in the nodes and you want to flatten the tree back into its original
sequence.

3) post-order traversal(left->right->root):
- visits all the leaves before visiting any nodes;
- used to delete leaf nodes from a tree.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


r"""                               # Node F is a root (topmost node of the tree). It's also the parent of nodes D and I.
          ______F______            # Nodes D and I are child nodes of F.
         /             \           # D and all its child notes are subtree.
      __D__           __I__        # A, C, E, H and J are leaf nodes - they have no child nodes.
     /     \         /     \
    B       E       G       J
   / \               \
  A   C               H
"""


def preorder_print(root, path=""):
    """Root->Left->Right"""
    if root:
        path += str(root.data) + "-"
        path = preorder_print(root.left, path)  # doesn't go on to the next function call until finishes all recursive calls
        path = preorder_print(root.right, path)
    return path


def inorder_print(root, path=""):
    """Left->Root->Right"""
    if root:
        path = inorder_print(root.left, path)
        path += str(root.data) + "-"
        path = inorder_print(root.right, path)
    return path


def postorder_print(root, path=""):
    """Left->Right->Root"""
    if root:
        path = postorder_print(root.left, path)
        path = postorder_print(root.right, path)
        path += str(root.data) + "-"
    return path


if __name__ == '__main__':
    # Set up tree:
    root = Node("F")
    root.left = Node("D")
    root.left.left = Node("B")
    root.left.left.left = Node("A")
    root.left.left.right = Node("C")
    root.left.right = Node("E")
    root.right = Node("I")
    root.right.left = Node("G")
    root.right.left.right = Node("H")
    root.right.right = Node("J")

    print("Preorder:", preorder_print(root))
    print("Inorder:", inorder_print(root))
    print("Postorder", postorder_print(root))

r"""
          ______F______
         /             \
      __D__           __I__
     /     \         /     \
    B       E       G       J
   / \               \
  A   C               H
"""
