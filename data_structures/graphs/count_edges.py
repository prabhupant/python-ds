"""
Count the number of edges in an undirected graph

Use Handshaking Lemma (Note: Handshaking Lemma is only for undirected graph)

For all v in V, deg(v) = 2|E|
"""

Time - O(V)

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for i in range(vertices)]


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def count_edges(self):
        s = 0

        for i in range(self.V):
            s += len(self.graph[i])

        return s // 2


g = Graph(9)
g.add_edge(0, 1 )  
g.add_edge(0, 7 )  
g.add_edge(1, 2 )  
g.add_edge(1, 7 )  
g.add_edge(2, 3 )  
g.add_edge(2, 8 )  
g.add_edge(2, 5 )  
g.add_edge(3, 4 )  
g.add_edge(3, 5 )  
g.add_edge(4, 5 )  
g.add_edge(5, 6 )  
g.add_edge(6, 7 )  
g.add_edge(6, 8 )  
g.add_edge(7, 8 )

print(g.count_edges())