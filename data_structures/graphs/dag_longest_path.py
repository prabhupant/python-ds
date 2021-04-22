"""
The idea is similar to DAG Shortest Path. Only the comparision part changes
"""

from collections import defaultdict

class Graph:


    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices


    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))


    def topological_sort_util(self, vertex, visited, stack):
        visited[vertex] = True

        for v, weight in self.graph[vertex]:
            if visited[v] == False:
                self.topological_sort_util(v, visited, stack)

        stack.insert(0, vertex)


    def topological_sort(self):
        visited = [False] * self.vertices
        stack = []

        for v in range(self.vertices):
            if visited[v] == False:
                self.topological_sort_util(v, visited, stack)
        
        return stack


    def longest_path(self, s):
        stack = self.topological_sort()

        distance = [-float("inf")] * self.vertices
        distance[s] = 0

        while stack:
            i = stack.pop(0)

            for vertex, weight in self.graph[i]:
                if distance[vertex] < distance[i] + weight:
                    distance[vertex] = distance[i] + weight

        for i in range(self.vertices):
            print(f"{s} -> {i} = {distance[i]}")


g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 6)
g.add_edge(1, 2, 2)
g.add_edge(2, 4, 4)
g.add_edge(2, 5, 2)
g.add_edge(2, 3, 7)
g.add_edge(3, 5, 1)
g.add_edge(3, 4, -1)
g.add_edge(4, 5, -2)

source = 0

g.longest_path(source)