class Graph:

    def __init__(self, vertices, directed: bool):
        self.V = vertices
        self.e = 0
        self.d = directed
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)]

    def add_edge(self, ver1, ver2):
        if self.d:
            self.graph[ver1][ver2] = 1
        else:
            self.graph[ver1][ver2] = 1
            self.graph[ver2][ver1] = 1

    def remove_edge(self, ver1, ver2):
        if self.graph[ver1][ver2] == 0:
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

if __name__=="__main__":
    g1 = Graph(3,0)
    g1.add_edge(0,0)
    g1.add_edge(1,1)
    g1.add_edge(2,2)
    g1.remove_edge(2,1)
    g1.print_graph()

