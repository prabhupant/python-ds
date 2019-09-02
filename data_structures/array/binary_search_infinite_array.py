def binary_search(arr, start, end, val):
    while start <= end:
        mid = (start + end)//2
        if val == arr[mid]:
            return mid
        elif val > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def search(arr, val):
    if len(arr) == 1:
        if arr[0] == val:
            return "Found"
        else:
            return "Not found"
    
    temp = arr[0]
    low = 0
    high = 1

    while temp < val:
        low = 0
        high = 2 * high
        temp = arr[high]

    ans = binary_search(arr, low, high, val)

    if ans == -1:
        return "Not Found"
    else:
        return "Found at index {}".format(ans)


arr = [1,3,5,6,7,8,9,11,13,15,19]

print(search(arr, 7))
