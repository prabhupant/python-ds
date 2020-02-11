# Use backtracking
# The only with this approach is that if there is a cycle, then
# it can show infinitely many paths
# Reference - https://www.geeksforgeeks.org/count-possible-paths-two-vertices/

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)]


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def count_paths_util(self, u, v, visited, counter):
        visited[u] = True
        
        # If the destination vertex is found
        if u == v:
            counter[0] += 1

        else:
            for i in range(len(self.graph[u])):
                if not visited[self.graph[u][i]]:
                    self.count_paths_util(self.graph[u][i], v, visited, counter)

        visited[u] = False


    def count_paths(self, u, v):
        visited = [False] * self.vertices

        counter = [0]

        self.count_paths_util(u, v, visited, counter)

        return counter[0]


g = Graph(4)
g.add_edge(0, 1)  
g.add_edge(0, 2)  
g.add_edge(0, 3)  
g.add_edge(2, 0)  
g.add_edge(2, 1)  
g.add_edge(1, 3)

print(g.count_paths(2, 3))
