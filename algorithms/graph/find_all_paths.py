"""
find all the possible paths in a directed cyclic graph from
a start point to a end point.
"""


def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:  # to prevent cyclic rotations
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


# TESTING
GRAPH = {1: [2, 4],
         2: [3],
         4: [5],
         3: [5]
         }

for i in GRAPH.keys():
    print(i, 'to 5', find_all_paths(GRAPH, i, 5))
