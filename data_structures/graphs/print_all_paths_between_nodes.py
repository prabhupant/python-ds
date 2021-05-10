from collections import defaultdict

class Graph:


    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def print_path(self, s, d, visited, path):
        visited[s] = True
        path.append(s)

        if s == d:
            print(path)

        else:
            for i in self.graph[s]:
                if visited[i] == False:
                    self.print_path(i, d, visited, path)

        # If path from this node does not lead to the destination, remove it
        # from the path stack and mark it as not visited
        path.pop()
        visited[s] = False
        

    def print_all_paths(self, s, d):
        visited = [False] * self.vertices
        path = []
        self.print_path(s, d, visited, path)


g = Graph(4)

g.add_edge(0, 3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 0)
g.add_edge(2, 1)

s = 2
d = 3

print(f'Paths from {s} to {d} are - ')
g.print_all_paths(s, d)