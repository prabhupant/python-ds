{\rtf1\ansi\ansicpg1252\cocoartf2509
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Python program for implementation of heap Sort \
\
# To heapify subtree rooted at index i. \
# n is size of heap \
def heapify(arr, n, i): \
	largest = i # Initialize largest as root \
	l = 2 * i + 1	 # left = 2*i + 1 \
	r = 2 * i + 2	 # right = 2*i + 2 \
\
	# See if left child of root exists and is \
	# greater than root \
	if l < n and arr[i] < arr[l]: \
		largest = l \
\
	# See if right child of root exists and is \
	# greater than root \
	if r < n and arr[largest] < arr[r]: \
		largest = r \
\
	# Change root, if needed \
	if largest != i: \
		arr[i],arr[largest] = arr[largest],arr[i] # swap \
\
		# Heapify the root. \
		heapify(arr, n, largest) \
\
# The main function to sort an array of given size \
def heapSort(arr): \
	n = len(arr) \
\
	# Build a maxheap. \
	for i in range(n, -1, -1): \
		heapify(arr, n, i) \
\
	# One by one extract elements \
	for i in range(n-1, 0, -1): \
		arr[i], arr[0] = arr[0], arr[i] # swap \
		heapify(arr, i, 0) \
\
# Driver code to test above \
arr = [ 12, 11, 13, 5, 6, 7] \
heapSort(arr) \
n = len(arr) \
print ("Sorted array is") \
for i in range(n): \
	print ("%d" %arr[i]), \
}