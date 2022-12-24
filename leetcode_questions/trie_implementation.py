"""
208 leetcode problem
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.end_of_word

    def starts_with(self, prefix: str) -> bool:
        current = self.root

        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True


prefix_tree = PrefixTree()
prefix_tree.insert("apple")
print(prefix_tree.search("app"))
print(prefix_tree.search("apple"))

print(prefix_tree.starts_with("ape"))
print(prefix_tree.starts_with("ap"))
