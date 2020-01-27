# Reference - https://www.geeksforgeeks.org/roots-tree-gives-minimum-height/

from collections import defaultdict
from queue import Queue

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.degree = [0] * vertices


    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)
        self.degree[v] += 1
        self.degree[w] += 1


    def root_min_height(self):
        q = Queue()

        for i in range(self.V):
            if self.degree[i] == 1:
                q.put(i)


        while self.V > 2:
            for i in range(q.qsize()):
                t = q.get()
                self.V -= 1

                # For each neighbour decrease its degree and if it becomes
                # leaf, insert into the queue
                for j in self.graph[t]:
                    self.degree[j] -= 1
                    if self.degree[j] == 1:
                        q.put(j)


        res = list()
        while q.qsize() > 0:
            res.append(q.get())


        return res

g = Graph(6)
g.add_edge(0, 3) 
g.add_edge(1, 3) 
g.add_edge(2, 3) 
g.add_edge(4, 3) 
g.add_edge(5, 4) 

print(g.root_min_height())
