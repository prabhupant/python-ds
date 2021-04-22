def duplicate(arr):
    res = []
    for x in arr:
        if arr[abs(x) - 1] < 0:
            res.append(abs(x))
        else:
            arr[abs(x) - 1] *= -1
    return res
