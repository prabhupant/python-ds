def max_sum(arr):
    arr.sort()
    return sum(arr[-3:-1])+arr[-1] #Sum last three elements after sorting


arr = [1,3,6,3,6,8,3,3,7,9,4,-1,-1]

print(max_sum(arr))
