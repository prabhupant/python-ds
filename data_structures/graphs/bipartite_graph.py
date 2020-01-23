# Check for bipartite graph

# Do a BFS and make source of red color and its neighbour blue
# Keep on doing this.
# If self loop, return false
# If current color == neighbour color, false, else true

# Reference - https://www.geeksforgeeks.org/bipartite-graph/

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def is_bipartite(self, s):
        # 0 -> color 0
        # 1 -> color 1
        # -1 -> no color assigned

        colors = [-1] * self.V
        colors[s] = 1

        queue = []
        queue.append(s)

        while queue:
            u = queue.pop()

            if self.graph[u][v] == 1: # Check for self loop
                return False
            
            # An edge u to v exists and destination is not 
            # colored
            for v in range(self.V):
                if self.graph[u][v] == 1 and colors[v] == -1:
                    colors[v] = 1 - colors[u]
                    queue.append(v)

                elif self.graph[u][v] == 1 and colors[v] == colors[u]:
                    return False

        return True
