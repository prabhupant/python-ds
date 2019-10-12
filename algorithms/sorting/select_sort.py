def selection_sort(arr):
    """
    Selection Sort is an algorithm for finding the kth smallest number in a list or array;
    such a number is called the kth order statistic. This includes the cases of finding the minimum,
    maximum, and median elements.

    Ref: https://en.wikipedia.org/wiki/Selection_algorithm
    https://www.geeksforgeeks.org/selection-sort/

    The time complexity of selection sort is O(n^2).

    :param arr:
    :return:

    Examples:

    >>> selection_sort([100, 5, 72, 41, 80, 1, 99, 36, 27, 78])
    [1, 5, 27, 36, 41, 72, 78, 80, 99, 100]
    >>> selection_sort([10, 30, 20, 100, 40, 80, 90, 210, 34])
    [10, 20, 30, 34, 40, 80, 90, 100, 210]
    >>> selection_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> selection_sort([2, 3, 5, 0, 9, 1])
    [0, 1, 2, 3, 5, 9]

    """
    for i, _ in enumerate(arr):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
