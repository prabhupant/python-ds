def intersection(arr1, arr2):
    res = []
    i, j = 0, 0 
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            res.append(arr1[i])
            i += 1
            j += 1
    return res

arr1 = [1,2,3,4,5,6,7,8]
arr2 = [2,4,6,8]

print(intersection(arr1, arr2))

