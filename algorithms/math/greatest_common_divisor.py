def iterative_gcd(x, y):
    """
    High Level Description:
    Given two input integers, find their Greatest Common Divisor.

    Time Complexity:
    O(log(n))

    :param x:
    :param y:
    :return:

    Examples:
    >>> iterative_gcd(8, 12)
    4
    >>> iterative_gcd(54, 24)
    6

    """
    if x == 0:
        return y
    if y == 0:
        return x

    while x % y != 0:
        rem = x % y
        x = y
        y = rem

    return y


def recursive_gcd(x, y):
    """
    High Level Description:
    Given two input integers, find their Greatest Common Divisor.

    Time Complexity:
    O(log(n))

    :param x:
    :param y:
    :return:

    Examples:
    >>> recursive_gcd(8, 12)
    4
    >>> recursive_gcd(54, 24)
    6

    """
    if x == 0:
        return y
    if y == 0:
        return x

    return recursive_gcd(y, x % y)


if __name__ == "__main__":
    import doctest

    doctest.testmod()