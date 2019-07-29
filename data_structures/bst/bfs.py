import collections 

class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root):
    if not root:
        return
    
    queue = collections.deque([root])

    while queue:
        temp = queue.popleft()
        print(temp.val)
        if temp.right:
            queue.append(temp.right)
        if temp.left:
            queue.append(temp.left)


root = Node(3)
root.right = Node(4)
root.left = Node(2)

root.left.left = Node(1)
root.left.right = Node(2.5)

root.right.left = Node(3.5)
root.right.right = Node(5)

bfs(root)
