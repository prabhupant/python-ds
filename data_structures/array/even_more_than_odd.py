# Rearrange an array such that numbers at even indexes are greater than numbers 
# at odd indexes

def rearrange(arr):
    for i in range(1, len(arr)):
        if i % 2 == 0:
            if arr[i] > arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
        else:
            if arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
    print(arr)


arr = [ 1, 3, 2, 2, 5 ]
rearrange(arr)