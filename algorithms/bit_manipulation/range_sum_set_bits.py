# Question: Find the sum of number of set bits in all the numbers in the range [1, n].

def countBits(n):
    
    """ Consider a number x and half of the number (x//2).
    The binary representation of x has all the digits as
    the binary representation of x//2 followed by an additional
    digit at the last position. Therefore, we can find the number
    of set bits in x by finding the number of set bits in x//2
    and determining whether the last digit in x is 0 or 1. """

    res = [0] * (n+1)
    for i in range(1, n+1):
        res[i] = res[i//2] + (i & 1)
    return sum(res)
    

# Extension: Find the sum of number of set bits in all the numbers in the range [m, n].
# Answer: In countBits(m, n), return sum(res) - sum(res[:m])