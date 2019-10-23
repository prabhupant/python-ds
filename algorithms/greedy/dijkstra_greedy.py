def dijkstra(graph, start, end):
    shortest_distance = {}
    non_visited_nodes = {}
    for i in graph:
        non_visited_nodes[i] = graph[i]
        
    infinit = float('inf')

    for no in non_visited_nodes:
        shortest_distance[no] = infinit
    shortest_distance[start] = 0
    
    while non_visited_nodes != {}:
        shortest_extracted_node = None
        for i in non_visited_nodes:
            if shortest_extracted_node is None:
                shortest_extracted_node = i
            elif shortest_distance[i] < shortest_distance[shortest_extracted_node]:
                shortest_extracted_node = i

        for no_v, Weight in graph[shortest_extracted_node]:
            if Weight + shortest_distance[shortest_extracted_node] < shortest_distance[no_v]:
                shortest_distance[no_v] = Weight + shortest_distance[shortest_extracted_node]
        non_visited_nodes.pop(shortest_extracted_node)
    return shortest_distance

#in this case, I made a graph within the code, but I didn't put here, you can create your graph the way you like.
#this algorithm needs the start, end, and weight, but you can remove the weight as well
#I will leave my example here, how I use this algorithm to solve the shortest path problem
# V is vertex, u is edges and W IS WEIGHT.

cities, origin, destiny = map(int, input().split())
graph = {i:[] for i in range(1, cities+1)}
for i in range(cities-1):
    u, v, w = map(int, input().split())
    graph[v].append((u, w))
    graph[u].append((v, w))