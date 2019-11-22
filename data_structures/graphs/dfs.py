from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append[v]


    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)


    def dfs(self, v):
        visited = [False] * (len(self.graph))
        self.dfs_util(v, visited)
