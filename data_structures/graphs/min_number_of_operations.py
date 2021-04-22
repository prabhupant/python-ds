"""
Minimum number of operations required to transform a number x to y
Valid operations - multiplication by 2, subtraction by 1
Ex - x = 4, y = 7
1. 4 * 2 = 8
2. 8 - 1 = 7
Answer = 2
"""


from collections import defaultdict


class Node:


    def __init__(self, value, level):
        self.value = value
        self.level = level


def min_steps(x, y):
    node_x = Node(x, 0)

    visited = []
    queue = []
    queue.append(node_x)

    while queue:
        s = queue.pop(0)

        if s.value == y:
            return s.level

        visited.append(s.value)

        if s.value * 2 == y or s.value - 1 == y:
            return s.level + 1

        # If not visited already, add its children

        if s.value * 2 not in visited:
            new_node = Node(s.value * 2, s.level + 1)
            queue.append(new_node)
        
        if s.value - 1 not in visited:
            new_node = Node(s.value - 1, s.level + 1)
            queue.append(new_node)


x = 2
y = 5

print(min_steps(x, y))