def rotate(arr, d):
    return arr[d:]+arr[:d]

arr = [1,2,3,4,5]
print(rotate(arr, 1))
