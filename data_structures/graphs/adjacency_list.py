class AdjNode():

    def __init__(self, val):
        self.vertex = val
        self.next = None


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # adding in undirected graph
    def add_edge(self, src, dest):
        # adding node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding source node to the destination as it is an
        # undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node


    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


