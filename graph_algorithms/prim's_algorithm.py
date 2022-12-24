"""
Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.
"""
import math


def get_min(list_of_edges, num_connected_nodes)


# list of edges - length, node1, node2
list_of_edges = [(math.inf, -1, -1), (13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6), (26, 2, 3), (19, 2, 5),
                 (30, 3, 4), (22, 4, 6)]

num_nodes = 6  # number of nodes in the graph
num_connected_nodes = {1}  # set of connected nodes
spanning_tree_nodes = []  # list of edges in a spanning tree

while len(num_connected_nodes) < num_nodes:
    node = get_min(list_of_edges, num_connected_nodes)  # edge with a minimum weight
    if node[0] == math.inf:  # if no edges,
        break

    spanning_tree_nodes.append(node)  # adding a node to the spanning tree
    num_connected_nodes.add(node[1])  # adding nodes to a set of connected nodes
    num_connected_nodes.add(node[2])
