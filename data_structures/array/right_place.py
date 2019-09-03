def place(arr):
    for i in range(len(arr)):
        if arr[i] >= 0 and arr[i] != i:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        else:
            i += 1

arr = [-1,-1, 6,1,9,3,2,-1,4,-1]
place(arr)
print(arr)
