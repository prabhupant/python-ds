def longest_inc_subseq(l):
	n=len(l)
	LIS=[1]*(n)
	maximum=1
	for i in range(1,n):
		for j in range(0,i):
			if l[i]>l[j] and (LIS[i]<LIS[j]+1):
				LIS[i]=LIS[j]+1
			maximum=max(maximum,LIS[i])
	print(maximum)
arr=[10, 22, 9, 33, 21, 50, 41, 60] 
longest_inc_subseq(arr)
