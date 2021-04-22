"""
Check for bipartite graph

Do a BFS and make source of red color and its neighbour blue
Keep on doing this.
If self loop, return false
If current color == neighbour color, false, else true

Reference - https://www.geeksforgeeks.org/bipartite-graph/

A bipartite graph is a graph whose vertices can be divided into two disjoint sets U and V 
such that every edge connects a vertex in U to one in V. Also, a bipartite graph does not 
contain any odd length cycles

Also, a graph with no edge is a bipartite graph - https://math.stackexchange.com/a/53947
"""

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def bfs(self, s):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=' ')

            for i in self.graph[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)


    def is_bipartite(self, s):
        # 0 -> color 0 (blue)
        # 1 -> color 1 (red)
        # -1 -> no color assigned

        colors = [-1] * self.V
        colors[s] = 1  # Color soure vertex red

        queue = []
        queue.append(s)

        while queue:
            s = queue.pop(0)

            if s in self.graph[s]: # Check for self loop
                return False
            
            # An edge u to v exists and destination is not 
            # colored
            for i in self.graph[s]:
                if colors[i] == -1:
                    colors[i] = 1 - colors[s]
                    queue.append(i)

                elif colors[i] == colors[s]:
                    return False

        return True


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 0)
print(g.is_bipartite(0))