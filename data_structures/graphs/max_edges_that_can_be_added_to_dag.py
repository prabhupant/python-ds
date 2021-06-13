"""
Find the max number of edges that can be added to a Directed Acyclic Graph such that 
it remains a DAG.

Solution - 
The trick is to add all edges from left to right. Now adding any edge from right to left
will make the graph cyclic because that edge's counterpart will exist from left-to-right.
Hence a cycle will be formed.

1. Topologically sort all the edges
2. If edge is not there left to right, create the edge
3. Count the number of edges added

source - https://www.geeksforgeeks.org/maximum-edges-can-added-dag-remains-dag/

"""

from collections import defaultdict

class Graph:


    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, v)


    def topological_sort(self):
        visited = [False] * self.vertices
        stack = []

        for i in range(self.vertices):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        return stack

    
    def max_edges(self):
        topo = self.topological_sort()
        visited = [False] * self.vertices
        count = 0

        for i in range(len(topo)):
            vertex = topo[i]
            # Mark the connected vertices visited
            for j in self.graph[vertex]:
                visited[j] = True

            # Print the unmarked nodes from topo
            for j in range(i+1, len(topo)):
                if visited[topo[j]] == False:
                    print(f"{vertex} -> {topo[j]}")
                    count += 1
                
                visited[topo[j]] = False

        print('Maximum edges that can be added - ', count)


g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.max_edges()