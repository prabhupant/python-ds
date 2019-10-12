def max_sub_array(arr):
    """
    High Level Description:
    Given an integer array nums, find the contiguous subarray (containing at least
    one number) which has the largest sum and return its sum.

    Time Complexity: (Iterative Solution)
    O(n)

    :param arr:
    :return:

    Examples:
    >>> max_sub_array([2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    >>> max_sub_array([2, 2, -2])
    4

    """
    if not arr:
        return 0

    cur_sum = max_sum = arr[0]
    for num in arr[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)

    return max_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
