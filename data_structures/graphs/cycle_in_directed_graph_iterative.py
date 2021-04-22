from collections import defaultdict


class Graph:


    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def dfs(self):
        visited = [False] * self.vertices
        recursion_stack = [False] * self.vertices
        stack = []

        for v in range(self.vertices):
            if visited[v] == False:
                visited[v] = True
                recursion_stack[v] = True
            
                stack.append(v)

                while stack:
                    s = stack.pop()

                    recursion_stack[s] = True

                    for i in self.graph[s]:
                        if visited[i] == False:
                            stack.append(i)
                            visited[i] = True
                            recursion_stack[i] = True
                        elif recursion_stack[i] == True:
                            return "Contains Cycle"
                            
            recursion_stack[v] = False

        return "No cycle"


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print(g.dfs())