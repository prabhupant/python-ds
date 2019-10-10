"""
Question
You have been given a String S. You need to find and print whether this string is a palindrome or not. If yes, print "YES" (without quotes), else print "NO" (without quotes).
Source Hackerearth
Input Format:
The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.
ex: aba,abc
Output Format:
Print the required answer on a single line.
ex: YES,NO
"""

def palindrome(string):
    if(string==string[::-1]): # Check if string is equal to reverse of the string using string slicing method
        print('YES') # the print YES
    else:
        print('NO') # else print NO
string=input() # Take input string from the user
palindrome(string) # pass the input to the user defined function palindrome
