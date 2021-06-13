"""
Check if two nodes are on the same path in a undirected graph. Use DFS and the concept of intime and outtime.
Intime - time when a node is visited for the first time
Outtime - time when a node is visited for the second time after all its children have been visited
For any pair of node if they are on the same path -
intime[u] < intime[v] and outtime[u] > outtime[v]
"""

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def dfs(self, vertex, intime, outtime, timer, visited):
        visited[vertex] = True
        timer += 1
        intime[vertex] = timer

        for v in self.graph[vertex]:
            if visited[v] == False:
                self.dfs(v, intime, outtime, timer, visited)
        
        timer += 1
        outtime[vertex] = timer


    def on_same_path(self, u, v):
        intime = [-1] * self.vertices
        outtime = [-1] * self.vertices
        timer = 0
        visited = [False] * self.vertices

        for vertex in self.graph:
            if visited[vertex] == False:
                self.dfs(vertex, intime, outtime, timer, visited)

        
        if (intime[u] < intime[v] and outtime[u] > outtime[v]) \
            or (intime[v] < intime[u] and outtime[v] > outtime[u]):
            return True
        return False


g = Graph(9)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 5)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(4, 6)
g.add_edge(4, 7)
g.add_edge(4, 8)

print(g.on_same_path(0, 4))
print(g.on_same_path(1, 8))
print(g.on_same_path(1, 5))