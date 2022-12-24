class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        current = self.root
        while True:
            # to prevent from inserting a value that is already in th tree
            if new_node.value == current.value:
                return False
            if new_node.value < current.value:
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            else:  # elif new_node.value > current.value:
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right

    def breadth_first_search(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def __contains__(self, value):
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:  # if value == current.value:
                return True
        return False


my_tree = BinarySearchTree()
# print(my_tree.root.value)
# my_tree.insert(1)
# print(my_tree.root.left.value)
# my_tree.insert(3)
# print(my_tree.root.right.value)

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(27 in my_tree)
print(17 in my_tree)

print(my_tree.breadth_first_search())
print("-" * 10)
print(my_tree.dfs_pre_order())
print("-" * 10)
print(my_tree.dfs_post_order())
print("-" * 10)
print(my_tree.dfs_in_order())
