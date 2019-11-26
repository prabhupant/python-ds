# Print tree in a diagonal form

# We use the distance of slope from the rightmost slope as key 
# in a dict and then proceed

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diagonal_print_util(root, d, diagonal_map):
    if root is None:
        return

    try:
        diagonal_map[d].append(root.val)
    except:
        diagonal_map[d] = [root.val]

    # Increase vertical distance if left child
    diagonal_print_util(root.left, d+1, diagonal_map)

    # Vertical distance remains same for the right child
    diagonal_print_util(root.right, d, diagonal_map)


def diagonal_print(root):
    diagonal_map = dict()

    diagonal_print_util(root, 0, diagonal_map)
    
    for i in diagonal_map:
        for j in diagonal_map[i]:
            print(j, end=" ")
        print('')
