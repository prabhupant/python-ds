"""
---------------------------------------  Sum Of Array  ------------------------------------------

Given an array of length N, you need to find and return the sum of all elements of the array.
Do this recursively.

#### Input Format :
    Line 1 : An Integer N i.e. size of array
    Line 2 : N integers which are elements of the array, separated by spaces

#### Output Format :
    Sum

#### Constraints :
    1 <= N <= 10^3

#### Sample Input 1 :
    3
    9 8 9
#### Sample Output 1 :
    26

#### Sample Input 2 :
    3
    4 2 1
#### Sample Output 2 :
      
"""

def sumArray(arr): 
    n=len(arr) 
    if(n == 1): 
        return arr[0] 
    smallAns = sumArray(arr[:n-1]) 
    return smallAns + arr[n-1] 

# Main 
from sys import setrecursionlimit 
setrecursionlimit(11000) 
n=int(input()) 
arr=list(int(i) for i in input().strip().split(' ')) 
print(sumArray(arr))