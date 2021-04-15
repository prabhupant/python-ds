"""
Find if a graph can be divided into two cliques

A clique is a subgraph such that all vertices in it are completely
connected with each other

Solution - 
A bipartite graph is a graph which can be divided into two sets U and V such
that every edge from u or v has a destination in the other.
So take the complement of the graph (create edge where there is none, and destroy
edges where present) and if the complement is a bipartite, it means that there are edges
in U and V that connect each other. So complement's complement (i.e the original graph) will
not have these edges and hence it can be divided into two clique
"""

from collections import defaultdict

class Graph:


    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.cgraph = defaultdict(list)
        self.vertices = vertices

    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def is_bipartite(self):
        colors = [-1] * self.vertices
        queue = []

        for v in range(self.vertices):
            if colors[v] == -1:
                colors[v] = 1

                queue.append(v)

                while queue:
                    s = queue.pop(0)

                    for i in self.cgraph[s]:
                        if colors[i] == -1:
                            colors[i] = 1 - colors[s]
                            queue.append(i)

                        elif colors[i] == colors[s]:
                            return False

        return True

    
    def make_complement(self):
        for src, dest in self.graph.items():
            for v in range(self.vertices):
                if v not in dest and src != v:
                    self.cgraph[src].append(v)
                    self.cgraph[v].append(src)

    
    def two_cliques(self):
        self.make_complement()
        return self.is_bipartite()


g = Graph(5)
g.add_edge(0, 3)
g.add_edge(3, 4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
print(g.two_cliques())