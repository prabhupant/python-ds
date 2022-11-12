"""
-------------------------------------------- Pair star -----------------------------------------

Given a string S, compute recursively a new string where identical chars that are adjacent in the original 
string are separated from each other by a "*".

#### Input format :
    String S

#### Output format :
    Modified string

#### Constraints :
    0 <= |S| <= 1000
    where |S| represents length of string S.

#### Sample Input 1 :
    hello
#### Sample Output 1:
    hel*lo

#### Sample Input 2 :
    aaaa
#### Sample Output 2 :
    a*a*a*a
"""

def pair_star(s,start,end):
    if start==end:
        return s[start]
    if s[start]==s[start+1]:
        return s[start]+"*"+pair_star(s,start+1,end)
    else:
        return s[start]+pair_star(s,start+1,end)
    
# Main 
s=input()
print(pair_star(s,0,len(s)-1))
