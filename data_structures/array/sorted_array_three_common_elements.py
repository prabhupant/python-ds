def common(arr1, arr2, arr3):
    res = []
    i, j, k = 0, 0, 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            res.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return res

arr1 = [1,2,3,4,5,6,7,8,9, 10, 11 ,12]
arr2 = [2,4,6,8, 10, 12]
arr3 = [3,6,9, 12]

print(common(arr1, arr2, arr3))
