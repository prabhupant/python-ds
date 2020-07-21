"""
Given two input integers, find their Least Common Multiple.
"""

from greatest_common_divisor import gcd


def lcm(x, y):
    return abs(x * y) // gcd(x, y)


# TESTING
if __name__ == "__main__":
    assert lcm(360, 84) == 2520
    assert lcm(2**10, 3**10) == 2**10 * 3**10
    print("Tests pass.")
