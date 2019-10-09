def maximum_sum_subseq(l):
	n=len(l)
	LIS=l.copy()
	maximum=l[0]
	for i in range(1,n):
		for j in range(0,i):
			if l[i]>l[j] and (LIS[i]<LIS[j]+l[i]):
				LIS[i]=LIS[j]+l[i]
			maximum=max(maximum,LIS[i])
	print(maximum)
arr=[10, 22, 9, 33, 21, 50, 41, 60] 
maximum_sum_subseq(arr)
