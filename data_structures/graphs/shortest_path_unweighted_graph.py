"""
Find the shortest path between two nodes in an unweighted undirected graph. Remember this
is about finding the shortest path, not the shortest distance. For shortest
distance you can simply calculate the level of nodes from the source vertex
and that will give the answer. For shortest path, use the concept of parents of 
Bellman-Ford algorithm.

Simply do a BFS and keep track of parents of each node. Then recursively print the 
parents of destination node until the source node.
"""

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    
    def bfs(self, s):
        parent = [-1] * self.vertices
        visited = [False] * self.vertices
        visited[s] = True
        queue = []
        queue.append(s)

        while queue:
            s = queue.pop(0)

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    parent[i] = s
                    visited[i] = True
        
        return parent

    
    def shortest_path(self, source, dest):
        parent = self.bfs(source)

        while True:
            print(dest, end=' ')
            dest = parent[dest]

            if dest == source:
                break


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(3, 4)
g.add_edge(3, 7)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(4, 7)
g.add_edge(5, 6)
g.add_edge(6, 7)

g.shortest_path(0, 7)