def pivot(arr):
    s = sum(arr)
    left_sum = 0
    for i, x in enumerate(arr):
        if left_sum == (s - x - left_sum):
            return i
        left_sum += x
    return -1
