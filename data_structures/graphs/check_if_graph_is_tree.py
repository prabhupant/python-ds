"""
A graph is a tree if -
1. It does not contain cycles
2. The graph is connected

Do DFS and see if every vertex can be visited from a source vertex and check for cycle
"""

from collections import defaultdict

class Graph:


    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def is_tree(self, s):
        visited = [False] * self.vertices
        parent = [-1] * self.vertices
        stack = []

        visited[s] = True
        no_of_visited = 1
        stack.append(s)

        while stack:
            s = stack.pop()

            for i in self.graph[s]:
                if visited[i] == False:
                    parent[i] = s
                    visited[i] = True
                    stack.append(i)
                    no_of_visited += 1
                elif parent[s] != i:
                    return "Not a tree"

        if no_of_visited == self.vertices:
            return "Graph is Tree"
        else:
            return "Not a tree"

        
g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 6)

print(g.is_tree(0))