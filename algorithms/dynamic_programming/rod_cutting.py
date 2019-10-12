INT_MIN = -32767


def cut_rod(price):
    """
    Given a rod of length n units and an
    array of prices that contains prices
    of all pieces of size less than n. We
    need to find the maximum maximum price
    obtainable by cutting the rod and
    selling it.


    :param price: List[int]
    :return int: max price

    Examples:

    >>> cut_rod([1, 5, 8, 9, 10, 17, 17, 20])
    22

    """
    n = len(price)
    values = [0 for _ in range(n + 1)]
    values[0] = 0

    for i in range(1, n + 1):
        max_value = INT_MIN
        for j in range(i):
            max_value = max(max_value, price[j] + values[i - j - 1])
        values[i] = max_value

    return values[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
