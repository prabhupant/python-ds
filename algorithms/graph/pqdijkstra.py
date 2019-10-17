from collections import defaultdict
from heapq import heappush, heappop

# Example graph: {0: [(3, 1), (4, 2)], 1: [(3, 3)]}
# Node 0 has an edge to 1 with distance 3.


def dijkstra(graph, start):
    queue = []
    heappush(queue, (0, start))
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    while queue:
        distance, node = heappop(queue)
        if distances[node] < distance:
            continue
        try:
            for d, neighbor in graph[node]:
                new_distance = distance+d
                if new_distance < distances[neighbor]:
                    heappush(queue, (new_distance, neighbor))
                    distances[neighbor] = new_distance
        except:
            continue
    return distances

if __name__ == '__main__':
    graph = {0: [(3, 1), (4, 2)], 1: [(3, 3)], 2: [(1, 3), (5, 0)]}
    print(dijkstra(graph, 0))
