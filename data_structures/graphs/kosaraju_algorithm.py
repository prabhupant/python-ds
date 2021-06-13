"""
Reference - https://www.geeksforgeeks.org/strongly-connected-components/

Algorithm - https://youtu.be/RpgcYiky7uw

This is used to find all the strongly connected components and does DFS
2 times.

Note: A single vertex is also strongly connected
"""

from collections import defaultdict


class Graph:


    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def fill_time(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.fill_time(i, visited, stack)

        stack = stack.append(v)


    def dfs(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs(i, visited)

    
    def create_tranpose(self):
        tgraph = Graph(self.vertices)

        for i in self.graph:
            for j in self.graph[i]:
                tgraph.add_edge(j, i)

        return tgraph

    
    def kosaraju(self):
        visited = [False] * self.vertices
        stack = []

        for v in range(self.vertices):
            if visited[v] == False:
                self.fill_time(v, visited, stack)

        tgraph = self.create_tranpose()
        visited = [False] * self.vertices

        while stack:
            s = stack.pop()

            if visited[s] == False:
                tgraph.dfs(s, visited)
                print()     


g = Graph(11)
g.add_edge(0, 1)
g.add_edge(2, 0)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 3)
g.add_edge(6, 5)
g.add_edge(6, 7)
g.add_edge(7, 8)
g.add_edge(8, 9)
g.add_edge(9, 10)
g.kosaraju()