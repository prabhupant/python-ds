
def binary_search(arr, val):
    firstIdx = 0 
    lastIdx = len(arr) - 1

    if firstIdx > lastIdx: 
        return -1

    midIdx = (firstIdx + lastIdx)//2

    if(arr[midIdx] == val):
        return val
    elif(arr[midIdx] > val):
        return binary_search(arr[0:midIdx], val)
    elif(arr[midIdx] < val):
        return binary_search(arr[midIdx + 1:], val)


arr = [1,3,4,5,13,20,25,40,42,44,53]

print("FOUND::::::" + str(binary_search(arr,7)))