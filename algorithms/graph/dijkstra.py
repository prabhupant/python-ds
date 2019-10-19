import sys

class graph():

    def __init__(self, nodes):

        self.nodes = nodes
        self.graph = [[0 for column in range(nodes)]
                      for row in range(nodes)]
        self.dist = [sys.maxint]*self.nodes #Minimum distance continer
        self.spt_set = [False]*self.nodes #To check for spanning tree

    def min_distance(self):

        min_val = sys.maxint
        for v in range(self.nodes):
            if self.dist[v] < min_val and not self.spt_set[v]:
                min_val = self.dist[v]
                min_index = v

        return min_index

    def Dijkstra(self, src):

        self.dist[src] = 0
        for v in range(self.nodes):

            u = self.min_distance()
            self.spt_set[u] = True
            for v in range(self.nodes):
                if self.graph[u][v] > 0 and self.spt_set[v] == False and self.dist[v] > self.dist[u] + self.graph[u][v]:
                    self.dist[v] = self.dist[u] + self.graph[u][v]

        self.print_result()

    def print_result(self):

        for v in range(self.nodes):
            print (str(v) + "-->" + str(self.dist[v]))


g = graph(9)
'''
    Graph representation using matrix
'''
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.Dijkstra(0);