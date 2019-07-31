def sort_parity(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] % 2 > arr[j] % 2:
            arr[i], arr[j] = arr[j], arr[i]
        if arr[i] % 2 == 0:
            i += 1
        if arr[j] % 2 == 1:
            j -= 1

arr = [5,6,4,3,2,4,5,6,7,8,9,8,7,4]

sort_parity(arr)
print(arr)
