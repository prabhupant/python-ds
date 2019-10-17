def shell_sort(arr):
    n = len(arr)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]

            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap = int(gap / 2)

    for i in arr:
        print(i)

# arr = [12, 45, 10, -1, 9, 14]

# print(shell_sort(arr))