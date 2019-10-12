def sieve(n):
    """
    Description:
    Sieve of Eratosthenes is a very fast method (loglog(n)) of finding primes upto a given number.
    :param n: int
    :return List[int]: prime numbers up to n including n

    Examples:
    >>> sieve(10)
    [2, 3, 5, 7]
    >>> sieve(31)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    """
    num_table = []
    primes = []
    for i in range(2, n + 1):
        if i not in num_table:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                num_table.append(j)
    return primes


if __name__ == "__main__":
    import doctest

    doctest.testmod()
