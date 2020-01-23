# The code is almost same to BFS, the only difference being queue
# is replaced by stack

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def dfs(self, s):
        visited = [False] * self.V

        stack = []

        stack.append(s)

        while stack:
            s = stack[-1]
            stack.pop()

            if not visited[s]:
                print(s, end=' ')
                visited[s] = True

            for i in self.graph[s]:
                if not visited[i]:
                    stack.append(i)



