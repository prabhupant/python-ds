"""
Question: Given a sentence containing n words/strings. 
Remove all duplicates words/strings which are similar to each others.
Example:
        Input: cat is cat
        Output: cat is
"""
#solution for the above question
from collections import Counter 

def remov_duplicates(input): 
  
    # split input string separated by space 
    input = input.split(" ") 
  
    # joins two adjacent elements in iterable way 
    for i in range(0, len(input)): 
        input[i] = "".join(input[i]) 
  
    # now create dictionary using counter method 
    # which will have strings as key and their  
    # frequencies as value 
    UniqW = Counter(input) 
  
    # joins two adjacent elements in iterable way 
    s = " ".join(UniqW.keys()) 
    print (s) 