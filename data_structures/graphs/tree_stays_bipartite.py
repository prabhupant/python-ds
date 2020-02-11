# All trees are bipartite graphs
# Reference - https://www.geeksforgeeks.org/maximum-number-edges-added-tree-stays-bipartite-graph/

# Traverse the tree (dfs or bfs) and color nodes with two colors and count each like
# count_color1 and count_color2. Then the max edges that the graph can have are
# count_color1 * count_color2, and the max edges of a tree are n-1

# Therefore the answer is = count_color1 * count_color2 - (n-1)

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)]

    
    def add_edge(self, u, v):
        self.graph[u].append(v)


    def bfs(self, s):
        visited = [False] * self.vertices
        color_count = [0, 0]

        colors = [-1] * self.vertices
        colors[s] = 1

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            
            for v in self.graph[u]:
                if colors[v] == -1: # This is a tree. So not visited and not colored is same as there is no cycle
                    colors[v] = 1 - colors[u]
                    queue.append(v)
                    color_count[colors[v]] += 1
                    visited[v] = True

        # Counting the max number of edges for graph
        graph_edges = color_count[0] * color_count[1]
        
        return graph_edges


# Number of tree nodes 
n = 5

g = Graph(5)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
