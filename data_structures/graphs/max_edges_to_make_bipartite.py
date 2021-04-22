"""
Find the max edges that can be added to a tree so that it stays a bipartite graph

keep count of nodes of each color - say count_color1, count_color2
These nodes can be connected in count_color1 x count_color2 ways = max no of edges of a bipartite graph
Also, a tree has n-1 edges
So answer = (count_color1 x count_color2) - (n - 1)

If the answer comes negative, then its impossible to add any edge because of odd cycles
"""

from collections import defaultdict

class Graph:


    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    
    def bfs(self, s):
        count_color0 = 0
        count_color1 = 0

        colors = [-1] * self.vertices
        colors[s] = 1
        count_color1 += 1

        queue = []
        queue.append(s)

        while queue:
            s = queue.pop(0)

            for i in self.graph[s]:
                if colors[i] == -1:
                    colors[i] = 1 - colors[s]
                    if colors[i] == 0:
                        count_color0 += 1
                    else:
                        count_color1 += 1
                    queue.append(i)
        
        ans = (count_color0 * count_color1) - (self.vertices - 1) 
        return ans if ans > 0 else 0 


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print(g.bfs(0))