# Move all zeros in an array to the end


def move(arr):
    count = 0
    for a in arr:
        if not a == 0:
            arr[count] = a
            count += 1
    while count < len(nums):
        arr[count] = 0
        count += 1
