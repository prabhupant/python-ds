# Python Program for implementation of 
# Recursive Bubble sort 
# Here we are working out the bubble sort algorithm within a recursive function.

# How to implement it recursively?
#Recursive Bubble Sort has no performance/implementation advantages, but can be a good question to check #one’s understanding of Bubble Sort and recursion.
#If we take a closer look at Bubble Sort algorithm, we can notice that in first pass, we move largest #element to end (Assuming sorting in increasing order). In second pass, we move second largest element to # 3second last position and so on.

# Recursion Idea.
#    1. Base Case: If array size is 1, return.
#    2. Do One Pass of normal Bubble Sort. This pass fixes last element of current subarray.
#    3. Recur for all elements except last of current subarray.

def bubble_sort(array): 
	for i, num in enumerate(array): 
		try: 
			if array[i+1] < num: 
				array[i] = array[i+1] 
				array[i+1] = num 
				bubble_sort(array) 
		except IndexError: 
			pass
	return array 

array = list(map(int, input().split())) 
bubble_sort(array) 

print("Sorted array:")
for i in range(0, len(array)): 
	print(array[i], end=' ') 



