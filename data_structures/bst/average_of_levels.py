import collections

class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def mean(arr):
    m = 0
    for x in arr:
        m += x
    return m / len(arr)


def bfs(root):
    if not root:
        return
    queue = collections.deque([root])
    result = []
    while queue:
        next_queue = collections.deque()
        for node in queue:
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        result.append(mean(queue))
        queue = next_queue
    return result

