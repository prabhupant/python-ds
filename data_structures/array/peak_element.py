# A peak element is an element such that both of its neighbours are smaller than it
# In case of corner elements, consider only one neighbour


def peak(arr, low, high):
    n = len(arr)

    while low <= high:
        mid = (high - low) // 2
        
        if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == n-1 or arr[mid+1] <= arr[mid]):
            return(arr[mid])

        elif mid > 0 and arr[mid-1] > arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

arr = [1, 3, 20, 4, 1, 0]
print(peak(arr, 0, len(arr) - 1))