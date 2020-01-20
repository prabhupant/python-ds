# Find the common elements in three arrays

def find_common(arr1, arr2, arr3):
    i, j, k     = 0, 0, 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            print(arr1[i])
            i += 1
            j += 1
            k += 1

        elif arr1[i] < arr2[j]:
            i += 1

        elif arr2[j] < arr3[k]:
            j += 1

        else: 
            k += 1

arr1 = [1,2,3,4,5,6]
arr2 = [5,6,7,8,9]
arr3 = [4,5,6,9,10]

find_common(arr1, arr2, arr3)
