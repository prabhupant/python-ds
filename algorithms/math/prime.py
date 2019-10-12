import math


def is_prime(n):
    """
    High level description

    A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
    A natural number greater than 1 that is not prime is called a composite number.

    Time Complexity:
    O(sqrt(n))


    :param n:
    :return: True if n is prime, False otherwise

    Examples:
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(21)
    False
    >>> is_prime(998423)
    True
    >>> is_prime(998422)
    False
    """

    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    limit = int(math.sqrt(n)) + 1

    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
