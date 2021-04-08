"""
This is almost same as the iterative one for directed graph but we cannot use the 
concept of recursion stack here because in directed graphs, there is defined path to
traverse but in undirected its possible that an edge (or a path) can be traversed
infite number of times.

Instead check for parents. If a parent of a node is visited and 
"""