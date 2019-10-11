#Uses adjacency matrix representation of graph to calculate Minimum Spanning Tree

import sys

class Graph():
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    
    #Function to print generated MST
    def printMST(self, parent):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    #Function to find vertex with min. distance from set of vertices
    #not included in MST
    def minValue(self, key, MSTSet):
        minval = sys.maxsize

        for v in range(self.V):
            if (key[v] < minval) and (MSTSet[v] == False):
                minval = key[v]
                min_index = v
        return min_index

    #Function to construct Prim's MST
    def MST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        MSTSet = [False] * self.V
        parent[0] = -1

        for j in range(self.V):
            u = self.minValue(key, MSTSet)
            MSTSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0) and (MSTSet[v] == False) and (key[v] > self.graph[u][v]):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

g = Graph(4)
g.graph = [ [0, 2, 0, 6],
            [2, 0, 3, 8],
            [0, 3, 0, 0],
            [6, 8, 0, 0]]

g.MST()