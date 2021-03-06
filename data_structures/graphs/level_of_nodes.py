from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def print_levels(self, s):
        levels = [None] * self.vertices
        levels[s] = 0
        queue = []
        queue.append(s)

        while queue:
            s = queue.pop(0)

            for i in self.graph[s]:
                if levels[i] == None:
                    levels[i] = levels[s] + 1
                    queue.append(i)
         
        print('Node \t Level')
        for node, level in enumerate(levels):
            print(f'{node} \t {level}')

g = Graph(8)
g.add_edge(0, 1)  
g.add_edge(0, 2)  
g.add_edge(1, 3)  
g.add_edge(1, 4)  
g.add_edge(1, 5)  
g.add_edge(2, 5)  
g.add_edge(2, 6)  
g.add_edge(6, 7) 
g.print_levels(0)
        
