# The array is sorted in decreasing order

def count(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == 1 and (arr[mid + 1] == 0 or mid == high):
            return mid + 1
        if arr[mid] == 1:
            start = mid + 1
        else:
            end = mid - 1
    return 0


arr = [0,0,0,0]

print(count(arr))
