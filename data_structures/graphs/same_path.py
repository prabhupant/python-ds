"""
Check if two nodes are on the same path in a tree. Use DFS and the concept of intime and outtime.
Intime - time when a node is visited for the first time
Outtime - time when a node is visited for the second time after all its children have been visited
For any pair of node if they are on the same path -
intime[u] < intime[v] and outtime[u] > outtime[v]
"""

from collections import defaultdict

class Graph:


    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices
        self.intime = None
        self.outtime = None


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def dfs(self):
        visited = [False] * self.vertices
        intime = [0] * self.vertices
        outtime = [0] * self.vertices
        timer = 0
        num_children_visited = [0] * self.vertices
        
        for s in range(self.vertices):
            if not visited[s]:
                visited[s] = True

                stack = []
                stack.append(s)
                
                while stack:
                    s = stack.pop()
                    timer += 1
                    intime[s] = timer

                    for i in self.graph[s]:
                        if visited[i] == False:
                            stack.append(i)
                            visited[i] = True
                            num_children_visited[s] += 1

                    if num_children_visited[i] == len(self.graph[i]):
                        timer += 1
                        outtime[i] = timer                  
                    
        print('intime - ', intime)
        print('outtime - ', outtime)
        print('num_children_visited - ', num_children_visited)
        self.intime = intime
        self.outtime = outtime


    def check_same_path(self, u, v):
        if (self.intime[u] < self.intime[v] and self.outtime[u] > self.outtime[v]) or \
                (self.intime[v] < self.intime[u] and self.outtime[v] > self.outtime[u]):
            return True
        return False


g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

g.dfs()

print('Same path - ', g.check_same_path(0, 6))
print(g.graph[6])