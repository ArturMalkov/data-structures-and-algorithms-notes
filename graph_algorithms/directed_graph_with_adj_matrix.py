class DirectedGraphAM:
    def __init__(self, size):
        self.vertices = {}  # dict of values that will keep track of all the edges emanating from a certain node
        self.size = size

    def add_edge(self, u, v, weight):  # u is the source node, v is the target node
        if u not in self.vertices:
            self.vertices[u] = {}

        self.vertices[u][v] = weight

    def get_neighbours(self, u):
        if u in self.vertices:
            for v in self.vertices[u]:
                yield v, self.vertices[u][v]  # returns a neighbor and associated weight

    def __repr__(self):
        rep = "graph: ["
        for u in range(self.size):  # we made the assumption at the beginning that all nodes will be identified by numbers between 0 and self.size - 1 to be able to use a for loop
            if u in self.vertices:
                rep += str(u) + ": "
                for v in self.vertices[u]:
                    rep += "(" + str(v) + ", " + str(self.vertices[u][v]) + "), "

        return rep + "]"


b = DirectedGraphAM(4)
b.add_edge(0, 2, 99)
print(b)
b.add_edge(0, 3, 88)
print(b)
b.add_edge(0, 2, 777)
print(b)

for neighbor in b.get_neighbours(0):
    print(neighbor)
