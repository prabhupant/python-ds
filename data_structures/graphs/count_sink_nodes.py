"""
Count the number of sink nodes

Sink nodes are the nodes without any outgoing edge

Solution - 
vertices contains the total number of edges and graph is an adjacency list.
Simply subtract the vertices and len(graph)
"""

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def count_sink_nodes(self):
        return self.vertices - len(self.graph)


g = Graph(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
print(g.count_sink_nodes())