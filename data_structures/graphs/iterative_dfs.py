# The code is almost same to BFS, the only difference being queue
# is replaced by stack

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def dfs(self):
        visited = [False] * self.vertices
        stack = []

        for s in range(self.vertices):
            if visited[s] == False:
                visited[s] = True
                
                stack.append(s)

                while stack:
                    s = stack.pop()
                    print(s, end=' ')

                    for i in self.graph[s]:
                        if visited[i] == False:
                            stack.append(i)
                            visited[i] = True


# g = Graph(4) 
# g.add_edge(0, 1) 
# g.add_edge(0, 2) 
# g.add_edge(1, 2) 
# g.add_edge(2, 0) 
# g.add_edge(2, 3) 
# g.add_edge(3, 3) 
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(3, 4)

g.dfs()
