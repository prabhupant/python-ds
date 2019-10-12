def climb_stairs(n):
    """
    High Level Description:
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you
    climb to the top?

    Time Complexity:
    O(n)

    :param n: int
    :return ans: int

    Examples:

    >>> climb_stairs(2)
    2
    >>> climb_stairs(10)
    89
    >>> climb_stairs(20)
    10946

    """
    if n == 0 or n == 1:
        return 1
    first = 1
    second = 1
    ans = 0

    for i in range(2, n + 1):
        ans = first + second
        second = first
        first = ans
    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
