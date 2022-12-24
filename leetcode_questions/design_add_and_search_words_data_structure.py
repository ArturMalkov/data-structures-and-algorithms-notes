"""
211 leetcode problem
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.end_of_word = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            current = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in current.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in current.children:
                        return False
                    current = current.children[c]

            return current.end_of_word

        return dfs(0, self.root)
