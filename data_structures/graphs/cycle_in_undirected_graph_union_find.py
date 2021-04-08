"""
This method cannot be used in Directed graph because of the direction of the edge.
In a union of set containing element A and B, you cannot specify whether A is going to B
or vice versa
"""

from collections import defaultdict


class Graph:


    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def union(self, parent, x, y):
        parent[x] = y


    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        else:
            return self.find_parent(parent, parent[i])

    
    def check_cyclic(self):
        parent = [-1] * self.vertices

        for i in self.graph.keys():
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)

                if x == y:
                    return "Cyclic"
                
                self.union(parent, x, y)

        return "Not cyclic"


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 3)
print(g.check_cyclic())