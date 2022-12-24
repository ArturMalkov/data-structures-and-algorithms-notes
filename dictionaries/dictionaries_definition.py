"""
Dictionaries (maps or associative arrays).

Dictionaries are indexed using keys instead of a numerical index (i.e. it uses non-numerical indexes).

Dictionaries are implemented using hash tables and keys in their key-value pairs are stored in memory in hash tables at
indexes which are determined by a hash function.

Hash function takes all the keys for a given dictionary and strategically maps them to certain index locations in a
hash table so that they can eventually be retrieved easily.

Hash collision - happens when we run two different dictionary keys into a hash function, and the computer tells us to store
them at the same index location?

2 ways to resolve hash collision:
1) open addressing:
- put the key in some other index location separate from the one returned to us by the hash function
(usually done by looking at the next null value in a hash table - i.e. closest location which contains no key).

2) closed addressing:
- uses linked lists to chain together keys which result in the same hash value.
Several keys are stored in a linked list at the same index location (which slows down accessing those elements to O(n)).
"""