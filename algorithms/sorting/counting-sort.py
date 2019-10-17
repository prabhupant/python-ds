{\rtf1\ansi\ansicpg1252\cocoartf2509
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Python program for counting sort \
\
# The main function that sort the given string arr[] in \
# alphabetical order \
def countSort(arr): \
\
	# The output character array that will have sorted arr \
	output = [0 for i in range(256)] \
\
	# Create a count array to store count of inidividul \
	# characters and initialize count array as 0 \
	count = [0 for i in range(256)] \
\
	# For storing the resulting answer since the \
	# string is immutable \
	ans = ["" for _ in arr] \
\
	# Store count of each character \
	for i in arr: \
		count[ord(i)] += 1\
\
	# Change count[i] so that count[i] now contains actual \
	# position of this character in output array \
	for i in range(256): \
		count[i] += count[i-1] \
\
	# Build the output character array \
	for i in range(len(arr)): \
		output[count[ord(arr[i])]-1] = arr[i] \
		count[ord(arr[i])] -= 1\
\
	# Copy the output array to arr, so that arr now \
	# contains sorted characters \
	for i in range(len(arr)): \
		ans[i] = output[i] \
	return ans \
\
# Driver program to test above function \
arr = "geeksforgeeks"\
ans = countSort(arr) \
print "Sorted character array is %s" %("".join(ans)) \
\
}