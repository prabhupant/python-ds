# An Iterative DFS solution.
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def DFS_util(self, s, visited):

        stack = []

        stack.append(s)

        while (len(stack) != 0):

            s = stack.pop()

            if (not visited[s]):
                print(s, end=" ")
                visited[s] = True

            i = 0
            while i < len(self.adj[s]):
                if (not visited[self.adj[s][i]]):
                    stack.append(self.adj[s][i])
                i += 1

    def DFS(self):
        visited = [False] * self.V
        for i in range(self.V):
            if (not visited[i]):
                self.DFS_util(i, visited)


if __name__ == '__main__':

    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(2, 1)
    g.add_edge(3, 4)
    g.add_edge(4, 0)

    print("Following is Depth First Traversal")
    g.DFS()
