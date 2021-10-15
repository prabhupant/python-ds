"""
Question
You are given a string S, check if all characters are unique.

SAMPLE INPUT 1
abcd
SAMPLE OUTPUT 1
True

SAMPLE INPUT 2
aabc
SAMPLE OUTPUT 2
False
"""
from collections import Counter
def unique_char_check(S):
    character_count = Counter(S)

    if len(character_count) == len(S):
        return True
    return False

S = input()
print(unique_char_check(S))