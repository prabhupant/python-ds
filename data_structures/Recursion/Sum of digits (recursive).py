"""
---------------------------- Sum of digits (recursive) ----------------------------

Write a recursive function that returns the sum of the digits of a given integer.

#### Input format :
    Integer N

#### Output format :
    Sum of digits of N

#### Constraints :
    0 <= N <= 10^9

#### Sample Input 1 :
    12345
#### Sample Output 1 :
    15

#### Sample Input 2 :
    9
#### Sample Output 2 :
    9
"""

def sumOfDigits(n): 
    if n == 0: 
        return 0 
    smallAns = sumOfDigits(n // 10) 
    return smallAns + n%10 
    
# Main 
from sys import setrecursionlimit 
setrecursionlimit(11000) 
n=int(input()) 
print(sumOfDigits(n))