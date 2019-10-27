from collections import defaultdict


def topological_sort(graph: dict) -> list:
    """Provides the topologically sorted nodes of a graph in a list.  Takes input as a dictionary,
    where the key is a node and the value is a list of the nodes that the key is a source node for."""

    # Keeps track of the "degree" of a node; once this reaches 0, we push it onto the output.
    leading_in = defaultdict(lambda: 0)

    for key, values in graph.items():
        if key not in leading_in.keys():
            leading_in[key] = 0
        for node in values:
            leading_in[node] += 1

    queue = []
    output = []

    for node, degree in leading_in.items():
        if degree == 0:
            queue.append(node)
            output.append(node)

    while queue:
        node = queue.pop(0)
        for destination in graph.get(node, []):
            leading_in[destination] -= 1
            if leading_in[destination] == 0:
                queue.append(destination)
                output.append(destination)

    return output
