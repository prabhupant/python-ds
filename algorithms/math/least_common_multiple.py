"""
Given two input integers, find their Least Common Multiple.
"""

from greatest_common_divisor import gcd

def lcm(x, y):
    return abs(x * y) // gcd(x, y)
