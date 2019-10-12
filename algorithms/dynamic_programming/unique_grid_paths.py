def number_of_paths(m, n):
    """
    High Level Description:
    A person is located at the top-left corner of a m x n grid (marked 'Start' in
    the diagram below). The person can only move either down or right at any point
    in time. The person is trying to reach the bottom-right corner of the grid
    (marked 'Finish' in the diagram below).
    How many possible unique paths are there?

    Time Complexity:
    O(m*n)

    :param m: int
    :param n: int
    :return int: Unique paths

    Examples:

    >>> number_of_paths(5, 4)
    35
    >>> number_of_paths(3, 4)
    10
    >>> number_of_paths(1, 5)
    1

    """
    count = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        count[i][0] = 1

    for j in range(n):
        count[0][j] = 1

    for i in range(1, m):
        for j in range(n):
            count[i][j] = count[i - 1][j] + count[i][j - 1]
    return count[m - 1][n - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
