# The only prerequisite condition of this algorithm is that the array
# definitely contains a majority element, otherwise it will just return
# the last element

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


arr = [3, 3, 1,5,6,8,3,0,7]

print(majority(arr))