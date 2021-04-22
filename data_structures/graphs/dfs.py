from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)


    def dfs(self, v):
        visited = [False] * (len(self.graph))
        self.dfs_util(v, visited)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
print(g.dfs(0))
