"""
Heap - recursive data structure.

Tree-based structure with following properties:
- Heap property: each node compares to its children in some specific way;
- Shape property: tree filled by level, left to right (guarantees that all heaps are balanced which helps to avoid O(n) time complexity (unlike in binary trees)).

Min-Heap:
- value at the root node of the tree must be the minimum amongst all its children.
- this fact must be the same recursively for all parent nodes contained within the heap.

Max-Heap:
- value at the root node of the tree must be the maximum amongst all its children.
- this fact must be the same recursively for all parent nodes contained within the heap.

Minimal structure has impressive characteristics:
- min in O(1);
- add and remove in O(log n).

Science of selecting a winner:

8 teams in a tournament:
28 possible games - (8 * 7) / 2
7 total games lead to winner
3-tier structure
log(8) = 3

A \
   winner \
B /
C \        winner \
   winner /        \
D /                 \
E \                   winner
   winner  \        /
F /                /
G \        winner /
   winner  /
H /

Use cases in programming:
- used in the implementation of HeapSort - a sorting algorithm which takes in a list of elements, builds them into a min
or max heap, and then removes the root node continuously to make a sorted list;
- used in the implementation of priority queues - which are used by a computer to designate tasks and assign computer
power based on how urgent the matter is.
"""


class Heap:
    def __init__(self, values=None):
        """Constructs list from values"""
        if values is None:
            self.ar = []
        else:
            self.ar = list(values)
        self.n = len(self.ar)

        start = self.n//2 - 1
        for i in range(start, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        """Converts structure rooted at self.ar[i] into a heap.
        Heapify sub-array [i, end). O(logN) operation - it only has to go down the height of the tree."""
        left = 2 * i + 1
        right = 2 * i + 2

        # Find smallest element of A[i], A[left], and A[right]
        if left < self.n and self.ar[left] < self.ar[i]:
            smallest = left
        else:
            smallest = i

        if right < self.n and self.ar[right] < self.ar[smallest]:
            smallest = right

        # If smallest is not already the parent, then swap and propagate
        if smallest != i:
            self.ar[i], self.ar[smallest] = self.ar[smallest], self.ar[i]
            self.heapify(smallest)

    def is_empty(self):
        """Determines whether a heap is empty."""
        return self.n == 0

    def pop(self):
        """Returns smallest value and repairs heap."""
        if self.n == 0:
            raise ValueError("Heap is empty.")
        val = self.ar[0]
        self.n -= 1
        self.ar[0] = self.ar[self.n]
        self.heapify(0)
        return val

    def add(self, value):
        """Adds value to heap and repairs heap."""
        if self.n == len(self.ar):
            self.ar.append(value)
        else:
            self.ar[self.n] = value
        i = self.n
        self.n += 1

        # Correct structure to root
        while i > 0:
            parent = (i-1) // 2
            if self.ar[i] < self.ar[parent]:
                self.ar[i], self.ar[parent] = self.ar[parent], self.ar[i]
                i = parent
            else:
                break

    def __len__(self):
        """Returns size of heap"""
        return self.n

    def __repr__(self):
        """Return representation of heap as an array"""
        return f"heap: [{', '.join(map(str, self.ar[:self.n]))}]"
