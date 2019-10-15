def max_ones(arr):
    maximum = 0
    count = 0
    for i in arr:
        if i == 1:
            count += 1
        if count > maximum:
            maximum = count
        if i == 0:
            count = 0
    return maximum
