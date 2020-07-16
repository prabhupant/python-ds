def lis(a):
    # n = length of array a. Subsequence must include a[n]
    n = len(a)

    # Create table T of size n, with all entries initialized to 1
    T = [1]*n

    # For each substring of a, find the longest increasing subsequence
    # Set the corresponding entry of T to its value
    for i in range (1 , n):
        for j in range(0 , i):
            if T[i] <= T[j] and a[i] > a[j]:
                T[i] = T[j] + 1

    # Length of the longest subsequence ending with the last value in a
    return T[n]
