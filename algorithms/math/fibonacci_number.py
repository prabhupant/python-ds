def fibonacci(n):
    """
    Int fibonacci sequence ach number in the sequence is
    the sum of the two numbers that precede it.
    Like so: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

    :param n:
    :return:

    Examples:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(7)
    13
    >>> fibonacci(10)
    55

    """
    fn_2 = 0
    fn_1 = 1

    if n == 0:
        return fn_2
    if n == 1:
        return fn_1
    fn = 0
    for _ in range(2, n + 1):
        fn = fn_1 + fn_2
        fn_2, fn_1 = fn_1, fn

    return fn


if __name__ == "__main__":
    import doctest

    doctest.testmod()
