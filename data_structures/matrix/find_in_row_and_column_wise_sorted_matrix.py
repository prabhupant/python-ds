def search(mat, n, x):

    i = 0

    j = n - 1

    while i < n and j >=0:
        if mat[i][j] == x:
            print("Found at - ", i, j)
            return 1
        if mat[i][j] > x:
            j -= 1
        else:
            i += 1

    print("Element not found")
    return 0
