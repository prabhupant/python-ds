"""
We are given a DAG. Find the smallest set of vertices from which all 
nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Solution - 
The crux of the question is that - 
1. If any node has an indegree > 1 (i.e it is reachable from any other node), then it means
in a connected graph it will be possible to reach here if its parent node also has an indegree
2. So the min will be the set of nodes with indegree = 0
"""

