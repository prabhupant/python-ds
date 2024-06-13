"""
---------------------------------------  String to Integer  --------------------------------------------

Write a recursive function to convert a given string into the number it represents. That is input will
be a numeric string that contains only numbers, you need to convert the string into corresponding integer 
and return the answer.

#### Input format :
    Numeric string S (string, Eg. "1234")

#### Output format :
    Corresponding integer N (int, Eg. 1234)

#### Constraints :
    0 <= |S| <= 9
    where |S| represents length of string S.

#### Sample Input 1 :
    1231
#### Sample Output 1 :
    1231

#### Sample Input 2 :
    12567
#### Sample Output 2 :
    12567
"""

def string_int(s,end):
    if end==0:
        return ord(s[0])-48
    b=ord(s[end])-48
    return b + 10*string_int(s,end-1)
    
# Main
s=input()
print(string_int(s,len(s)-1))