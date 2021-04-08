"""
Using three colors - white, gray and black
White - vertices that are not processed (inital state of all vertices)
Gray - vertices that are in DFS
Black - fully traversed vertices (i.e its progenies are also done)

If while traversing any adjacent node is colored Gray, that means cycle exists
"""  

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def detect_cycle(self):
        color = ['white'] * self.vertices
        visited = [False] * self.vertices

        stack = []

        for v in range(self.vertices):
            if color[v] == 'white':
                color[v] = 'gray'

                stack.append(v)

                while stack:
                    s = stack.pop()

                    for i in self.graph[s]:
                        if color[i] == 'white':
                            stack.append(i)
                            color[i] = 'gray'
                        elif color[i] == 'gray':
                            return "Cycle detected"

            color[v] = 'black'
        
        return "Cycle not present"


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 3)
print(g.detect_cycle())