# Topological sorting of Directed Acyclic Graph
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):

        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, v)

    # Topological sort function
    def topologicalSort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if (visited[i] == False):
                self.topologicalSortUtil(i, visited, stack)

        print(stack)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("One possible Topological Sort of the graph is:")
g.topologicalSort()
