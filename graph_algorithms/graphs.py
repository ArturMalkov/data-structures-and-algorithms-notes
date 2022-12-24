"""
Graph - nonlinear data structure consisting of nodes (node or vertex) + edges (any connections between any pair of nodes)
Unlike trees, graphs have no specified starting points - we can begin at any node.

Directed graphs' edges have directions (arrows): "A -> B" (one-way street)
Undirected graphs' edges do not have directions (arrow heads): "A - B" (two-way street - can move in any direction)
(i.e. they are bidirectional).
All undirected graphs are cyclical.

Neighbors = nodes accessible through an edge (obeying its direction)

Graph info is represented in code in adjacency list (suitable for sparse graphs (i.e. when there are not so many edges))
(it can also be represented visually using adjacency matrix - suitable for dense graphs with lots of edges (i.e. when
it's more likely than not that there's an edge between any two vertices)):
{
    a: [b, c],
    b: [d],
    c: [e],
    d: [],
    e: [b],
    f: [d]
}
- keys are nodes in the graph (even nodes with no neighbors);
- values are neighbors of the corresponding nodes.

Cyclic graphs - have cycles among nodes (leading to infinite loops).
Acyclic graphs - do not have cycles among nodes.

Weighted vs unweighted graphs:
- associating a numerical value with each edge (cost - e.g. cost of shipping goods via a particular route);
- each weight represents some property of information you're trying to convey (e.g. distance between nodes).

Use cases in programming:
The most famous implementation of graph - undirected cyclical graph with weighted edges -
used through Dijkstra's shortest path algorithm - used in Google Maps.

Use cases in real world:
- unweighted cyclical graphs are used in the follower system of a majority of social media websites (Facebook, etc.);
- network routing protocols also use graphs with weighted edges.

P.S. linked lists are forms of trees (with some limitations), trees are forms of graphs (with some limitations) =>
linked lists are forms of graphs (with some limitations).

Big O:
- space complexity:
in adjacency matrix - O(v**2), where 'v' is the number of vertices (since each vertex has to store all the vertices it is
not connected to);
in adjacency list - O(v + e), where 'v' is the number of vertices and 'e' is the number of edges.

- time complexity:
a) adding a vertex (without connecting it with anything via edges):
in adjacency matrix - O(v**2), where 'v' is the number of vertices (we're rewriting the entire matrix: adding a new row +
adding a new column);
in adjacency list - O(1) (simply adding a new key-value pair to a dictionary).
b) adding an edge:
O(1) for both an adjacency matrix and an adjacency list (changing 0s to 1s for adjacency matrix/appending new values to
lists of neighboring vertices for adjacency list).
c) removing an edge:
in adjacency matrix - O(1) (simply changing 0s to 1s);
in adjacency list - O(e), where 'e' is the number of edges (iteration through the list of neighbouring vertices).
d) removing a vertex:
in adjacency matrix - O(v**2), where 'v' is the number of vertices (we're rewriting the entire matrix - removing a row and a column);
in adjacency list - O(v + e), where 'v' is the number of vertices and 'e' is the number of edges (we need to iterate through
a list of edges associated with each vertex).

Python 3rd party libraries implementing graph data structure:
- Python-graph
- iGraph
- Networkx
"""


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ": ", self.adj_list[vertex])


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")


my_graph.add_edge("A", "B")
my_graph.add_edge("B", "D")
my_graph.add_edge("D", "C")
my_graph.add_edge("C", "A")
my_graph.add_edge("A", "D")

# my_graph.print_graph()

my_graph.remove_vertex("D")
my_graph.print_graph()
#
# # my_graph.remove_edge("A", "B")
#
# my_graph.print_graph()
# print("---")
#
# my_graph.remove_vertex("C")
# my_graph.print_graph()
