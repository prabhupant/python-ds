# Given an array containing only 0s, 1s and 2s in a random order, arrange the array such that all 0s come 
# before 1s which in turn come before all 2s
# Input - [1,2,0,1,2,1,0,1,2,1,0]
# Output - [0,0,0,1,1,1,1,1,2,2,2]

def dutch(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


arr = [1,0,2,1,0,2,1,2,1,2,1,1,0,2,1,0,1,2,1,2,1,1,2,1,0,2,1,1]
print(arr)
dutch(arr)
print(arr)

