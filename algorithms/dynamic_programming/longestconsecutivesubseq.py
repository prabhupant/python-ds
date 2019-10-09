def longest_consecutive_subseq(l):
	s=set()
	for i in l:
		s.add(i)
	maximum=l[0]
	for i in range(len(l)):
		if arr[i]-1 not in s:
			j=arr[i]
			while(j+1 in s):
				j=j+1
			maximum=max(maximum,j-arr[i]+1)
	print(maximum)
arr = [1, 9, 3, 10, 4, 20, 2]
longest_consecutive_subseq(arr)
