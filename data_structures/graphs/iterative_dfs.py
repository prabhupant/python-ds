# The code is almost same to BFS, the only difference being queue
# is replaced by stack

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def dfs(self, s):
        visited = [False] * len(self.graph)

        stack = []

        stack.append(s)
        visited[s] = True

        while stack:
            s = stack.pop()
            print(s, end=' ')

            for i in self.graph[s]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True


g = Graph() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 

g.dfs(0)
