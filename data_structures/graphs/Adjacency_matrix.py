class Graph:

    def __init__(self, vertices, directed: bool):
        self.V = vertices
        self.e = 0
        self.d = directed
        self.graph = []
        for i in range(self.V):
            lst = [0] * self.V
            self.graph.append(lst)

    def add_edge(self, ver1, ver2):
        if self.d:
            self.graph[ver1][ver2] = 1
        else:
            self.graph[ver1][ver2] = 1
            self.graph[ver2][ver1] = 1

    def remove_edge(self, ver1, ver2):
        if self.d[ver1][ver2] == 0:
            print("No edge between %d and %d" % (ver1, ver2))
            return
        if self.d:
            self.graph[ver1][ver2] = 0
        else:
            self.graph[ver1][ver2] = 0
            self.graph[ver2][ver1] = 0

    def print_graph(self):
        for i in self.graph:
            print(i)




