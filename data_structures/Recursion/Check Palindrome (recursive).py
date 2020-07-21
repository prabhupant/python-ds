"""
----------------------------  Check Palindrome (recursive)  -----------------------------

Check whether a given String S is a palindrome using recursion. Return true or false.

#### Input Format :
    String S

#### Output Format :
    'true' or 'false'

#### Constraints :
    0 <= |S| <= 1000
    where |S| represents length of string S.

#### Sample Input 1 :
    racecar
#### Sample Output 1:
    true

#### Sample Input 2 :
    ninja
#### Sample Output 2:
    false
"""

def RcheckPalindrome(str): 
    size=len(str) 
    if size <= 1: 
        return True 
    if str[0]!=str[size-1]: 
        return False 
    return RcheckPalindrome(str[1:-1]) 
    
# Main 
from sys import setrecursionlimit 
setrecursionlimit(11000) 
str=input() 
if RcheckPalindrome(str): 
    print('true') 
else: 
    print('false')