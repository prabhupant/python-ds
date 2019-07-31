def majority(arr):
    maj_index = 0
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[maj_index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1

    return arr[maj_index]
