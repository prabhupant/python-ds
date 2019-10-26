# Find the first character in a string without using extra space
# With extra space its simple. Just check for the element in a hash map
# If present, then it is the recurrent char

# Without extra space idea -
# The idea is to use an integer variable and uses bits in its binary representation to store whether a 
# character is present or not. 
# Typically an integer has at-least 32 bits and we need to store presence/absence of only 26 characters.

def first_recurrence(s):
    checker = 0 
    pos = 0
    for i in s:
        val = ord(i) - ord('a')
        if (checker & (1 << val) > 0):
            return i
        checker = checker | (1 << val)
        pos += 1
    return -1
