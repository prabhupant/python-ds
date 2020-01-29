from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def dfs_util(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)


    def count_nodes(self, v):
        visited = [False] * self.V

        self.dfs_util(v, visited)

        count = 0

        for i in range(self.V):
            if visited[i] == False:
                count += 1

        return count

g = Graph(8)  
g.add_edge(0, 1)  
g.add_edge(0, 2)  
g.add_edge(1, 2)  
g.add_edge(3, 4)  
g.add_edge(4, 5)  
g.add_edge(6, 7)

print(g.count_nodes(0))
