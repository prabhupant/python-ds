# Program to check whether the given number is a power of two using bit manipulation

'''
Explanation
If a number is a power of two bitwise and of n and (n-1) is 0
Since this will not handle the case when n = 0, we make our result false
by ANDing our result with n when n = 0
''' 

import math

def is_power_of_two(num):
    return num and (not (num and (num-1)))

''' 
Example: num = 5
num = 101
num -1 = 100
num and (num - 1) = 4
'''

'''
Example: num = 4
num = 100 
num - 1 = 011
num and (num - 1) = 0 
'''

