"""
High Level Description:
Given two input integers, find their Greatest Common Divisor.

Time Complexity:
O(log(n))
"""
# Iterative Solution


def gcd(x, y):
    if x == 0:
        return y
    if y == 0:
        return x

    while x % y != 0:
        rem = x % y
        x = y
        y = rem

    return y

# Recursive Solution


def gcd(x, y):
    if x == 0:
        return y
    if y == 0:
        return x

    return gcd(y, x % y)


# Eucledean gcd algorithm
"""
It States that if we need to compute the gcd of x and y, We compute the equation x=qy+b in which
q=x//y and b=x%y and we continously change the values of q and b in which the next q:=b and
accordingly compute b. This goes on until b==0 and we take the preceding value of b.
"""


def gcd(K, M):
    k = max(K, M)
    m = min(K, M)
    while (m != 0):
        r = k % m
        k = m
        m = r
    return k
