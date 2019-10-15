# Python program to print topological sorting of a Directed Acyclic Graph
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def edge_add(self, u, v):
        self.graph[u].append(v)

    def topo_sort_stack(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topo_sort_stack(i, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):

        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topo_sort_stack(i, visited, stack)

        print stack


g = Graph(4)
g.edge_add(5, 2)
g.edge_add(5, 0)
g.edge_add(4, 0)
g.edge_add(4, 1)


print "Topological Sort of graph is:"
g.topological_sort()
