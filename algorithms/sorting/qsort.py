def qsort(arr):
    """
    High level explanation:
    Quicksort algorithm is that if we can efficiently partition a list,
    then we can efficiently sort it. Partitioning a list means that
    we pick a pivot item in the list, and then modify the list
    to move all items larger than the pivot to the right and all
    smaller items to the left.

    Once the pivot is done, we can do the same operation to the
    left and right sections of the list recursively until the list is sorted.

    Time complexity:
    Quicksort has a time complexity of O(n log n).

    :param arr:
    :return:


    Examples:

    >>> qsort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> qsort([2, 3, 5, 0, 9, 1])
    [0, 1, 2, 3, 5, 9]

    """
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    greater, lesser = [], []
    for item in arr:
        if item > pivot:
            greater.append(item)
        else:
            lesser.append(item)
    return qsort(lesser) + [pivot] + qsort(greater)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
