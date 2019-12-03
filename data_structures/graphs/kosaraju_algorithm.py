# Reference - https://www.geeksforgeeks.org/strongly-connected-components/

# This is used to find all the strongly connected components and does DFS
# 2 times.

from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)


    def fill_order(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.fill_order(i, visited, stack)
        stack.append(v)


    def get_transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)

        return g


    def kosaraju(self):
        stack = []
        visited = [False] * self.V

        for i in range(self.V):
            if visited[i] == False:
                self.fill_order(i, visited, stack)

        gr = self.get_transpose()

        visited = [False] * self.V

        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.dfs_util(i, visited)
                print()


