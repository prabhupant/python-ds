# Reference - https://www.geeksforgeeks.org/number-of-triangles-in-a-undirected-graph/
# Reference - https://www.geeksforgeeks.org/number-of-triangles-in-directed-and-undirected-graphs/

# In case of undirected graph - trace(A^3)/6
# For undirected graph, just check if an edge exists among all the three vertices

class Graph:

    def __init__(self, vertices, is_directed):
        self.V = vertices
        self.graph = [[] for i in range(vertices)]
        self.is_directed = is_directed


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def count_triangles(self):
        nodes = len(self.graph)
        count = 0

        for i in range(nodes):
            for j in range(nodes):
                for k in range(nodes):
                    if i != j and j != k and k != i and self.graph[i][j] and self.graph[j][k] and self.graph[k][i]:
                        count += 1

        return count // 3 if is_directed else count // 6
