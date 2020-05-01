def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    a = arr[0]
    b = arr[1]
    maxprod = a * b
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] * arr[j]) > maxprod:
                a = arr[i]
                b = arr[j]
                maxprod = a * b
    return maxprod
