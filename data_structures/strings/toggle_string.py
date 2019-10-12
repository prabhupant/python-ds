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

def toggle_string_1(string):
    return string.swapcase()

def toggle_string_2(string):
    toggle_string=''
    for s in string:
        if s.isupper():
            toggle_string+=s.lower()
        elif s.islower():
            toggle_string+=s.upper()
        else:
            toggle_string+=s
    return toggle_string

string=input()

# method 1
print(toggle_string_1(string)) 
# method 2
print(toggle_string_2(string))
