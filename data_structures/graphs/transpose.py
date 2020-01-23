from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def print_graph(self):
        for i in self.graph:
            print(i, " --> ", end=" ")
            for j in self.graph[i]:
                print(j, end=" ")
            print()

    
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)

        return g


g = Graph(5) 
g.add_edge(1, 0) 
g.add_edge(0, 2) 
g.add_edge(2, 1) 
g.add_edge(0, 3) 
g.add_edge(3, 4) 
g.print_graph()

print('---------')

t = g.transpose()
t.print_graph()
