def union(arr1, arr2):
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            res.append(arr2[j])
            j += 1
        else:
            res.append(arr1[i])
            res.append(arr2[j])
            i += 1
            j += 1

    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res


arr1 = [1,3,5,6,7,9]
arr2 = [2,4,5,8,10]

print(union(arr1, arr2))
        
