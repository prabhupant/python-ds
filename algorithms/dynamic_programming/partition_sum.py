# A Dynamic Programming based
# Python3 program to partition problem

# Returns true if arr[] can be partitioned
# in two subsets of equal sum, otherwise false
def find_partiion(arr, n) :
	sum = 0

	# Calculate sum of all elements
	for i in range(n) :
		sum += arr[i]
	if (sum % 2 != 0) :
		return 0
	part = [0] * ((sum // 2) + 1)

	# Initialize the part array as 0
	for i in range((sum // 2) + 1) :
		part[i] = 0

	# Fill the partition table in bottom up manner
	for i in range(n) :
	
		# the element to be included
		# in the sum cannot be
		# greater than the sum
		for j in range(sum // 2, arr[i] - 1, -1) :
		
			# check if sum - arr[i]
			# could be formed
			# from a subset
			# using elements
			# before index i
			if (part[j - arr[i]] == 1 or j == arr[i]) :
				part[j] = 1

	return part[sum // 2]

# Drive code
arr = [ 1, 3, 3, 2, 3, 2 ]
n = len(arr)

# Function call
if (find_partiion(arr, n) == 1) :
	print("Can be divided into two subsets of equal sum")
else :
	print("Can not be divided into two subsets of equal sum")
