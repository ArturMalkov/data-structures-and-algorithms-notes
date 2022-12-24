"""
Tree - a series of nodes and edges between them (parent-child relationships).
Trees - store data hierarchically as opposed to linearly.
Contain a series of linked nodes connected together to form a hierarchical representation of information.
Tree operates like a linked list where each node has the option of pointing towards multiple nodes.

Real-world examples: family tree, file structure, etc.

Nodes are also called vertices.
Edges - connections between nodes.

Root node has no parents (top-most node).
Nodes with the same parent are also referred to as siblings.
Leaf nodes have 0 children.

Properties:
- height (property of a tree): number of edges on the longest possible path down towards a leaf.
- depth (property of a node): number of edges required to get from that particular node to the root node.


Types:
- binary tries;
- tries;
- heaps;
- etc.

Binary search tree - recursive structure - grandfather of all recursive data structures:
- each node has at most 2 children and child on the left <= parent <= child on the right:
0 <= number of the children of a node <= 2;
- no two nodes can contain the same value;
- has exactly one root;
- exactly one path between root and any node (path is a series of connected nodes we can travel through).
(thus, cycles in a tree indicate that it's not a binary tree)

A tree with a root and a child (leaf) is still considered a binary tree.
A tree consisting of just a root is still considered a binary tree.
No nodes - empty tree - still a binary tree.

Operations' complexity:
1) O(log n) - biggest advantage of binary search tries:
  - search(val);
  - remove(val);
  - add(val);
(suppose we had a binary tree with 4 levels - it means we have (2**4 - 1) elements in it and it takes 4 steps to find/remove/add an element;
suppose we had a binary tree with 10 levels - it means we have (2**10 - 1) elements in it and it takes 10 steps to find/remove/add an element)
2) O(n):
  - iteration over all values.

Worst case of BST - a tree that never forks (i.e. always goes in the same direction - straight line) which is essentially a
linked list (e.g. 47 -> 76 -> 82 -> 91) => O(n) operations
(BST has faster lookup and removal (O(logN)) than a linked list while linked list has faster insertion (O(1)) than BST)
BUT
we still treat BST as O(logN) data structure.

Use cases in programming:
- used in database indexes.

Use cases in real world:
- file structure systems.
"""


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            # add to the left
            self.left = self.add_to_subtree(self.left, value)
        elif value > self.value:
            # add to the right
            self.right = self.add_to_subtree(self.right, value)

    @staticmethod
    def add_to_subtree(parent, value):  # helper method
        if parent is None:
            return BinaryNode(value)

        parent.add(value)  # double recursion
        return parent

    def remove(self, value):
        if value < self.value:
            self.left = self.remove_from_parent(self.left, value)
        elif value > self.value:
            self.right = self.remove_from_parent(self.right, value)
        else:
            if self.left is None:
                return self.right
            # if you want to remove the value, find the biggest value in left subtree
            child = self.left
            while child.right:
                child = child.right

            child_key = child.value
            self.left.remove_from_parent(self.left, child_key)
            self.value = child_key

        return self


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)

    def __contains__(self, target):
        node = self.root

        while node:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:  # if target == node.value:
                return True

        return False


if __name__ == '__main__':
    b_tree = BinaryTree()
    b_tree.add(7)
    print(b_tree.root.value)
    print(7 in b_tree)
    print(9 in b_tree)

    print("-----")
    b_tree.add(1)
    print(b_tree.root.value)
    print(b_tree.root.left.value)
