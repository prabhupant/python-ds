"""
This is almost same as the iterative one for directed graph but we cannot use the 
concept of recursion stack here because in directed graphs, there is defined path to
traverse but in undirected its possible that an edge (or a path) can be traversed
infite number of times.

Instead check for parents (which means vertex fro which you reached the current vertex). 
If a vertex is visited and you are not coming to this vertex from the current "source" vertex
(source - vertex from which DFS has started), then it means that in the same DFS chain, there is 
another path to reach this vertex - hence a cycle
"""

from collections import defaultdict

class Graph:


    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def dfs(self):
        visited = [False] * self.vertices
        parent = [-1] * self.vertices

        stack = []

        for v in range(self.vertices):
            if visited[v] == False:
                visited[v] = True
            
                stack.append(v)

                while stack:
                    s = stack.pop()

                    for i in self.graph[s]:
                        if visited[i] == False:
                            parent[i] = s
                            stack.append(i)
                            visited[i] = True
                        elif parent[s] != i:
                            return "Contains Cycle"

        return "No cycle"


g = Graph(5)
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)
print(g.dfs())