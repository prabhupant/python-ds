from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                if self.is_cyclic_util(i, visited, v):
                    return True

            elif parent != i:
                return True

        return False


    def is_cyclic(self):
        visited = [False] * (self.V)

        for i in range(self.V):
            if visited[i] == False:
                if self.is_cyclic_util(i, visited, -1):
                    return True

        return False
