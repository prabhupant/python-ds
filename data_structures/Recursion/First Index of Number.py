"""
--------------------------------------  First Index of Number  -----------------------------------------------

Given an array of length N and an integer x, you need to find and return the first index of integer x present 
in the array. Return -1 if it is not present in the array.

First index means, the index of first occurrence of x in the input array.
Do this recursively. Indexing in the array starts from 0.

#### Input Format :
    Line 1 : An Integer N i.e. size of array
    Line 2 : N integers which are elements of the array, separated by spaces
    Line 3 : Integer x

#### Output Format :
    first index or -1

#### Constraints :
    1 <= N <= 10^3

#### Sample Input :
    4
    9 8 10 8
    8
#### Sample Output :
    1
"""

def firstIndex(arr, x): 
    size=len(arr) 
    if size <= 0: 
        return -1 
    if x==arr[0]: 
        return 0 
    smallAns = firstIndex(arr[1:], x) 
    if smallAns == -1: 
        return -1 
    else: 
        return smallAns+1 
        
# Main 
from sys import setrecursionlimit 
setrecursionlimit(11000) 
n=int(input()) 
arr=list(int(i) for i in input().strip().split(' ')) 
x=int(input()) 
print(firstIndex(arr, x))