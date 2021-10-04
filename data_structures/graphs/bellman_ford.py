"""
Bellman Ford algorithm is used to find the single source shortest path in a weighted directed graph.
Example - find the shortest path from node A to F

Advantages of this algorithm over Djikstra's - 
1. Bellman Ford also works for negative weight edges
2. Also finds negative weight cycles in a graph 

Disvantage - 
1. Slower than Dijsktra's

** Idea (https://www.youtube.com/watch?v=-mOEd_3gTK0&t)

0. Shortest path can be found as -
if distance[v] > distance[u] + weight(u, v), then the right side is the shorter path
1. Mark parent and the new weight each time this is run
2. Do this V-1 times. In the first iteration, the algorithm will find the shortest path between the source
and source's neighbours
3. In the second, between source and source's neighbours' neighbours and so on (V - 1) times
4. Do this again. If in this Vth iteration, the weights of path decrease, then there is a negative cycle in the
graph

Time complexity - O(V * E)
Space complexity - O(V)
"""

from collections import defaultdict

class Edge:

    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight


class Graph:


    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices
        self.edges = {}


    def add_edge(self, u, v, weight):
        self.graph[u].append(v)
        self.edges[(u, v)] = Edge(u, v, weight)


    def bellman_ford(self, source, destination):
        parent = [-1] * self.vertices
        distance = [float("inf")] * self.vertices

        parent[source] = source
        distance[source] = source

        for i in range(self.vertices - 1):  # Doing V - 1 times to find shortest distance

            for (u, v) in self.edges:
                wt = self.edges[(u, v)].weight

                if distance[v] > distance[u] + wt:
                    distance[v] = distance[u] + wt
                    parent[v] = u

        # Now for the Vth iteration, check for the negative cycle

        negative_cycle_present = False
        
        for (u, v) in self.edges:
            wt = self.edges[(u, v)].weight
            if distance[v] > distance[u] + wt:
                negative_cycle_present = True
                break

        if negative_cycle_present:
            print('Contains negative cycle')
        else:
            print('No negative cycle')

        # Printing the shortest path from source to destination

        while True:
            print(f'{destination}', end=' ')
            destination = parent[destination]

            if destination == source:
                break         


g = Graph(5)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 5)
g.add_edge(0, 3, 8)
g.add_edge(1, 2, -3)
g.add_edge(2, 4, 4)
g.add_edge(3, 4, 2)
g.add_edge(4, 3, 1)

g.bellman_ford(0, 3)