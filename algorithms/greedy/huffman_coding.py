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