# Topological sorting of Directed Acyclic Graph
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):

        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, v)

    # Topological sort function
    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if (visited[i] == False):
                self.topological_sort_util(i, visited, stack)

        print(stack)


g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("One possible Topological Sort of the graph is:")
g.topological_sort()
