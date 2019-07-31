def move(arr):
    count = 0
    for a in arr:
        if not a == 0:
            arr[count] = a
            count += 1
    while count < len(nums):
        nums[count] = 0
        count += 1
