# Fast fibonacci using Matrix exponentiation

# | 1  1 |^n    | F(n+1)   F(n)  |
# | 1  0 |   =  |  F(n)   F(n-1) |

# So, if we want fibonacci's n-th number,
# | 1 1 1 0 |'s power of n is our result matrix
# and answer will be Matrix[0][1]

import numpy as np
from numpy.linalg import matrix_power

def fastFibo(n):
    i = np.array([[1, 1], [1, 0]])
    x = matrix_power(i, n)
    return x[0][1]

def main():
    print(fastFibo(1000))

main()