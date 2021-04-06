from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    
    def find_min_edges(self, u, v):
        visited = [False] * self.vertices
        distance = [0] * self.vertices
        queue = []

        queue.append(u)
        visited[u] = True

        while queue:
            s = queue.pop(0)

            for i in self.graph[s]:
                if visited[i] == False:
                    distance[i] = distance[s] + 1
                    queue.append(i)
                    visited[i] = True

        return distance[v]


g = Graph(9)

g.add_edge(0, 1)
g.add_edge(0, 7)
g.add_edge(1, 7)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(2, 8)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.add_edge(7, 8)

print(g.find_min_edges(0, 5))
