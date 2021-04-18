from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    
    def dfs(self, v, temp, visited):
        visited[v] = True
        temp.append(v)

        for i in self.graph[v]:
            if visited[i] == False:
                temp = self.dfs(i, temp, visited)

        return temp


    def connected_components(self):
        visited = [False] * self.vertices
        cc = []

        for i in range(self.vertices):
            if visited[i] == False:
                temp = []
                cc.append(self.dfs(i, temp, visited))

        return cc


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)

print(g.connected_components())                        