"""
Question
You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet 
in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted 
to uppercase. You need to then print the resultant String to output.
Source Hackerearth

SAMPLE INPUT 
abcdE
SAMPLE OUTPUT 
ABCDe
"""

def ToggleString1(string):
    return string.swapcase()

def ToggleString2(string):
    toggleString=''
    for s in string:
        if s.isupper():
            toggleString+=s.lower()
        elif s.islower():
            toggleString+=s.upper()
    return toggleString
           


string=input()
print(ToggleString1(string)) # method 1
print(ToggleString2(string)) # method 2
