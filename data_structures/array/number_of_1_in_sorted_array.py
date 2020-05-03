# The array is sorted in decreasing order


def count(array):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == 1 and (array[mid + 1] == 0 or mid == end):
            return mid + 1
        if array[mid] == 1:
            start = mid + 1
        else:
            end = mid - 1
    return 0


arr = [1, 1, 1, 1, 0, 0, 0, 0]

print(count(arr))
