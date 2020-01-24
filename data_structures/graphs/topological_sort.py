from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def topo_sort_util(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topo_sort_util(i, visited, stack)

        stack.insert(0, v)


    def topo_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topo_sort_util(i, visited, stack)

        print(stack)
