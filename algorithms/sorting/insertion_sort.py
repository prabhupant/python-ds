def insertion_sort(arr):
    """
    High Level Description:
    For every element in the given list, find its correct index by iterating
    backwards and finding a slot. This forms a sorted array.
    Time Complexity:
    Every element is visited, which contributes O(n). Swapping backwards takes
    O(n/2) time on average, meaning that the total complexity is O(n^2)

    :param arr:
    :return:

    Examples:
    >>> insertion_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> insertion_sort([2, 3, 5, 0, 9, 1])
    [0, 1, 2, 3, 5, 9]
    """
    for j, _ in enumerate(arr):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
