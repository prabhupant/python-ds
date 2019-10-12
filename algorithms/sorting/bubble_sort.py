def bubble_sort(arr):
    """
    Bubble Sort worst time complexity occurs when array is reverse sorted - O(n^2)
    Best time scenario is when array is already sorted - O(n)

    :param arr:
    :return: sorted array

    Examples:
    >>> bubble_sort([2, 3, 5, 0, 9, 1])
    [0, 1, 2, 3, 5, 9]
    """
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
