"""
Check if a string has unique chars
    
    How it works:
        - The total number of characters that a string can be built of is 128 chars,
          so if a string is longer than 128 chars, then it must have repeated chars.
        - if it's 128 or less, then check using two nested for loops.
"""
def unique_chars(s):
    lenS = len(s)
    if lenS > 128:
        return False
    for i in range(lenS-1):
        for j in range(i+1,lenS):
            if s[j]==s[i]:
                return False
    return True


s1 = "goToSchool"
s2 = "getAjob"
s3 = "A"

print("%s is: " %s1, unique_chars(s1), '\n')
print("%s is: " %s2, unique_chars(s2), '\n')
print("%s is: " %s3, unique_chars(s3), '\n')