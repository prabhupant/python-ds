"""
--------------------------------------   Count Zeros  -------------------------------------------

Given an integer N, count and return the number of zeros that are present in the given integer using recursion.

#### Input Format :
    Integer N

#### Output Format :
    Number of zeros in N

#### Constraints :
    0 <= N <= 10^9

#### Sample Input 1 :
    10204
#### Sample Output 1 :
    2

#### Sample Input 2 :
    708000
#### Sample Output 2 :
    4
"""

def countZeros(n): 
    if n<0: 
        n *= -1 # Make n positive 
    if n<10: 
        if n == 0: 
            return 1 
        return 0 
    smallAns = countZeros(n // 10) 
    if n%10==0: 
        smallAns += 1 
    return smallAns 
    
# Main 
from sys import setrecursionlimit 
setrecursionlimit(11000) 
n=int(input()) 
print(countZeros(n))