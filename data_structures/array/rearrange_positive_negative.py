# Rearragne positive and negative numbers in an array such that they appear
# alternately. If there are more numbers of any one kind, put them at the end

def rearrange(arr):
    i = -1

    for j in range(len(arr)):
        if arr[j] < 0:
            i += 1  # maintaining index of the last negative number
            arr[j], arr[i] = arr[i], arr[j]

    pos = i + 1  # index of first positive number
    neg = 0  # index of first negative number

    while pos < len(arr) and neg < pos and arr[neg] < 0:
        arr[pos], arr[neg] = arr[neg], arr[pos]
        pos += 1
        neg += 2

    print(arr)

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
rearrange(arr)