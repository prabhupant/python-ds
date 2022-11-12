"""
-------------------------------------- Remove X -------------------------------------

Given a string, compute recursively a new string where all 'x' chars have been removed.

#### Input format :
    String S
#### Output format :
    Modified String
#### Constraints :
    1 <= |S| <= 10^3
    where |S| represents the length of string S. 
#### Sample Input 1 :
    xaxb
#### Sample Output 1:
    ab
#### Sample Input 2 :
    abc
#### Sample Output 2:
    abc
"""

def removeX(string): 
    if len(string)==0: 
        return string 
    if string[0]=='x': 
        return removeX(string[1:]) 
    return string[0]+removeX(string[1:]) 

# Main 
string = input() 
print(removeX(string))