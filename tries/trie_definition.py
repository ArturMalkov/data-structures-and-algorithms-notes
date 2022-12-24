"""
Trie (or prefix tree) - a tree with special restrictions.

Nodes store letters of an alphabet in the form of characters.
We can carefully construct this tree of characters in such a way which allows us to quickly retrieve words in the form
of strings by traversing down a path of the trie in a certain way.

Flagging - marking the end of a word by having it also point towards a "flag" to let the computer know that the end of
a word has occurred.

Use cases in real world:
IOS and Google Docs store the entire English dictionary in a trie (each node has 26 nodes connected to it):
- text autocompletion;
- spellcheck.
"""


word_key = "\n"  # any character not in "a" ... "z"


def traverse(d, prefix):
    """Recursively generates all words in the Prefix Tree."""
    for k in d:
        if k == word_key:
            yield prefix
        else:
            for _ in traverse(d[k], prefix + k):
                yield _


class PrefixTree:
    def __init__(self, *start_values):
        self.head = {}
        self.count = 0
        self.num_dicts = 1
        for value in start_values:
            self.add(value.lower())

    def add(self, value):
        """Adds value to prefix tree. Return TRUE if updated."""
        d = self.head

        while len(value) > 0:
            if value[0] not in d:
                d[value[0]] = {}
                self.num_dicts += 1

            d = d[value[0]]
            value = value[1:]

        if word_key in d:
            return False

        d[word_key] = True
        self.count += 1
        return True

    def remove(self, value):
        """Remove value from prefix tree."""
        d = self.head
        while len(value) > 0:
            if value[0] not in d:
                return False

            d = d[value[0]]
            value = value[1:]

        if word_key not in d:
            return False
        del d[word_key]
        self.count -= 1
        return True

    def __contains__(self, value):
        """Determines if a value is present in the prefix tree."""
        d = self.head

        while len(value) > 0:
            if value[0] not in d:
                return False

            d = d[value[0]]
            value = value[1:]

        return word_key in d

    def __iter__(self):
        """Iterate over all values."""
        for _ in traverse(self.head, ''):
            yield _

    def __repr__(self):
        """Representation of the prefix tree."""
        return f"prefix: {self.count} entries in {self.num_dicts} dicts."

    def __len__(self):
        """Counts values in prefix tree."""
        return self.count


d = PrefixTree("in", "inch", "be", "bat")
print(d)
# print(d.add("in"))
# print(d.add("inch"))
# print(d.add("inch"))

print("str" in d)
print("inc" in d)
print("in" in d)
print("inch" in d)

for word in d:
    print(word)
