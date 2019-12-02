# https://www.geeksforgeeks.org/find-sum-nodes-given-perfect-binary-tree/

import math

def sum_nodes(l):
    leaf_nodes = math.pow(2, l-1)

    s = (leaf_nodes + (leaf_nodes + 1)) / 2

    res = s * l

    return int(res)
