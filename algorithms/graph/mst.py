# i checked your other py files and decided that i would go for default dict
# i used same structure as needed for this repository.
from collections import defaultdict
r = range


class Graph:
    # Class initializer
    def __init__(self, vertices):
        # num of vertices and our starting graph

        self.vertices = vertices
        # Values will be [start_point, end_point, weight]
        self.graph = []

    # Add edge to graph
    def add_edge(self, start, end, weight):
        value = [start, end, weight]
        self.graph.append(value)

    # Simple search alghoritm
    def search(self, parent_ranks, index):
        if parent_ranks[index] != index:
            return self.search(parent_ranks, parent_ranks[index])
        return index

    def union(self, ranks, parent_ranks, fir, sec):
        fir, sec = self.search(parent_ranks, fir), self.search(
            parent_ranks, sec)

        # 3 steps. ranks lower, higher, same

        if (ranks[fir] > ranks[sec]):
            parent_ranks[sec] = fir

        elif (ranks[fir] < ranks[sec]):
            parent_ranks[fir] = sec

        elif (ranks[fir] == ranks[sec]):
            parent_ranks[sec] = fir
            ranks[fir] += 1

    # run mst alghoritm main part.

    def run_mst(self, ranks, parent_ranks, answer):
        edge, index = 0, 0

        while True:
            if ((self.vertices - 1) <= edge):
                break

            # Take value
            value = self.graph[index]

            # check cycle
            fir, sec = self.search(parent_ranks, value[0]), self.search(
                parent_ranks, value[1])

            if fir != sec:
                edge += 1  # increase edge

                # append and union
                answer.append(value)
                self.union(ranks, parent_ranks, fir, sec)

            index += 1

    def print_graph(self, answer):
        for start, end, weight in answer:
            print(f"{start} - {end} --> {weight}")

    # Main function for mst alghoritm
    def MST(self):
        # sort the graph
        self.graph = sorted(self.graph, key=lambda item: item[2])

        # For this alghoritm we need two array.
        ranks = [0] * self.vertices
        parent_ranks = [_ for _ in r(self.vertices)]
        answer = []

        self.run_mst(ranks, parent_ranks, answer)
        self.print_graph(answer)
