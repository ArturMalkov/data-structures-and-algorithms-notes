"""
Hash tables are implemented in Python as dictionaries - sets of key-value pairs.
How hash table works?
Hash function/method (mathematical function) is performed on a key - when we run a key through a hash, in addition to
getting our key-value pair back, we get an address in memory (address space) where we store that key-value pair -
that is how a dictionary is stored.

2 characteristics of hash:
- one way: when we run a key through a hash and get an address in memory, we cannot undo the operation (i.e. take the
address in memory, run it through a hash and get a key back);
- deterministic: for a particular hash function, every time we put a particular key in it, we expect to get the same number every time.

Collisions in hash tables:
- happen when you put a key-value pair at an address where there was already a key-value pair.

Ways of dealing with collisions:
- Separate Chaining - a technique of dealing with collisions when you put key-value pairs at the same address.
- Linear Probing (one of the forms of open addressing - used in Python) - a technique of dealing with collisions when we already have a
key-value pair at the address a new key maps to - we go down until we find an empty address and put the key-value
pair there - applies when you don't have more than one key-value pair at any address.

In Python, 1/3 of hash table's elements must be empty - otherwise, array will be extended (needed to avoid the situation
when we have to search for an empty address/bucket too often - it negatively affects asymptotic behavior of a hash table).
Since 1/3 of an array is wasted, starting from Python 3.6 dictionary has a new internal structure - see the screen - it
allowed to save the memory and preserve the order in a dictionary (now only sets are unordered).


Big O of hash tables:
- all operations are considered O(1) operations (hash function itself is O(1), finding an address in memory is O(1) and
so is appending element to a particular slot in memory);
- worst case for getting an element - all the items are put to the same address: O(1) to find the address in memory but
O(n) to iterate through a list of collided keys to get to a particular key
BUT!
the assumption with hash tables is that the distribution of elements is going to be very efficient (and collisions will be fairly rare).

Why does hash map/hash table consist of immutable data types only?
When instantiating objects of immutable data types, we can calculate their hashes immediately (+ store as their property), and hashes won't change.
(extra bonus: we can compare immutable elements more quickly - if their hashes do not match, they are not equal, but if
there's a match - we need to check whether this is not a result of collision).
Otherwise, we'll need to recalculate hashes (after mutating elements) which requires iterating over the whole list +
we won't get an evenly distributed results of a hash function.
Thus, storing instances of immutable data types is the most efficient way of storing objects.

Problems with hash maps/hash tables:
- if we make it too big initially, it needs a lot of memory - O(n)
- if we make it too small initially, its fill ratio will be high (densely populated), thus leading to slow searches and deletes - O(k/n)
- we want to have a balance - e.g. fill ratio <= 1 - when the number of elements <= size of hash map/hash table - needed to
achieve O(1) complexity for all operations.

Solution to the problem:
- when hash table is filled (i.e. fill ratio is achieved - e.g. number of elements equal to its length), we increase its
size by 2 times and rebuild it (i.e. iterate over the entire hash table (O(n+k)), calculate new hash value for each element
and put it to a new address in the new hash table).
Amortized (!) complexity of such solution (average time for the operation) - O(n) - for adding n elements.
(Amortized complexity for adding 1 element1 is O(1) - but there were N operations and thus it took O(n).
In the worst case scenario, adding 1 element can be O(n) operation - if hash table was extended when adding that element).

Hash tables are used for:
- building caches;
- database indexes;
- etc.
"""


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size  # creating address space

    def __hash(self, key):  # this is what we pass the key to to determine the address at which to store a key-value pair
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)  # since the size of data_map is 7, the remainder (%) will always return values from 0 to 6
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


my_hash_table = HashTable()
my_hash_table.print_table()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("lumber", 70)
my_hash_table.print_table()


print(my_hash_table.get_item("bolts"))
print(my_hash_table.get_item("washers"))
print(my_hash_table.get_item("lumber"))
print(my_hash_table.get_item("nuclear bomb"))

print(my_hash_table.keys())
