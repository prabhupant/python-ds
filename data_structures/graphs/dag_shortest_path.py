"""
Find shortest path from source vertex to all vertices

In general, Bellaman-Ford and Dijkstra can be used to find shortest path. But for 
DAG, we can improvise

Bellman-Ford: O(V*E), Dijsktra: O(E+VlogV)

For DAG, using Topological sort will solve this problem in O(V+E). We are using Topo
sort because it lays out a graph in its linear representation according to the paths. 
Hence we can proceed in this order to find shortest path
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


    def shortest_path(self, s):
        stack = self.topological_sort()

        distance = [float("inf")] * self.vertices
        distance[s] = 0

        while stack:
            i = stack.pop(0)

            for vertex, weight in self.graph[i]:
                if distance[vertex] > distance[i] + weight:
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
g.add_edge(3, 4, -1)
g.add_edge(4, 5, -2)

source = 0

g.shortest_path(source)