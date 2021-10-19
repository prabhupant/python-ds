"""
In regular text file each character would take up 1 byte (8 bits) i.e. there are 16 characters
(including white spaces and punctuations) which normally take up 16 bytes.
In the ASCII code there are 256 characters and this leads to the use of 8 bits 
to represent each character but in any test file we do not have use all 256 characters.
For example, in any English language text, generally the character ‘e’ appears more than the character ‘z’.
To achieve compression, we can often use a shorter bit string to represent more frequently occurring characters.
We do not have to represent all 256 characters, unless they all appear in the document.
For optimal compression we use Huffman coding.

Solution:
A greedy algorithm constructs an optimal prefix code called Huffman code. 
The algorithm builds the tree T corresponding to the optimal code in a bottom-up manner. 
It begins with a set of |C| leaves (C is the number of characters) and perform |C| – 1 ‘merging’ 
operations to create the final tree.
In the Huffman algorithm ‘n’ denotes the number of set of characters, 
z denotes the parent node and x & y are the left & right child of z respectively.
"""
# A Huffman Tree Node
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''

# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree


def print_nodes(node, val=''):
    # huffman code for current node
    new_val = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        print_nodes(node.left, new_val)
    if(node.right):
        print_nodes(node.right, new_val)

        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {new_val}")


# characters for huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f']

# frequency of characters
freq = [ 5, 9, 12, 13, 16, 45]

# list containing unused nodes
nodes = []

# converting ccharacters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))

while len(nodes) > 1:
    # sort all the nodes in ascending order
    # based on theri frequency
    nodes = sorted(nodes, key=lambda x: x.freq)

    # pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]

    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1

    # combine the 2 smallest nodes to create
    # new node as their parent
    new_node = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

    # remove the 2 nodes and add their
    # parent as new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(new_node)

# Huffman Tree is ready!
print_nodes(nodes[0])