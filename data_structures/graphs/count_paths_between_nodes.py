from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def count_paths_util(self, u, d, visited, path_count):
        visited[u] = True

        if u == d:
            path_count[0] += 1

        else:
            i = 0
            for i in range(len(self.graph[u])):
                if not visited[self.graph[u][i]]:
                    self.count_paths_util(self.graph[u][i], d, visited, path_count)

        visited[u] = False


    def count_paths(self, s, d):
        visited = [False] * self.V
        path_count = [0]
        self.count_paths_util(s, d, visited, path_count)
        return path_count[0]


g = Graph(4)  
g.add_edge(0, 1)  
g.add_edge(0, 2)  
g.add_edge(0, 3)  
g.add_edge(2, 0)  
g.add_edge(2, 1)  
g.add_edge(1, 3)

s = 2
d = 3

print(g.count_paths(s, d))
