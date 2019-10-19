"""
Question:
Find the number of substrings in a given string which
start with a vowel. Compare this to the number of substrings
which start with a consonant. Determine which among them is higher.

Print 0 and number of substrings if number of substrings starting
with vowel is greater(or equal), 1 and number of substrings if
number of substrings starting with consonants is higher.

Example input: banana

Output: 1 12

Source : Hackerrank

Explanation:
It is interesting to note that in banana, number of letters = 6, and:

Substrings starting with first letter b    = 6
Substrings starting with second letter a   = 5
Substrings starting with third letter n    = 4
Substrings starting with fourth letter a   = 3
Substrings starting with fifth letter n    = 2
Substrings starting with last letter a     = 1

Hence we can form a total of 12(6 + 4 + 2) substrings starting with
consonants as compared to only 9(5 + 3 + 1) substrings starting
with vowels. Hence output is 1 12.

General Approach:
We can run a loop from the start to end of the string
and filter out substrings starting with vowels and constants.
"""

def count_substrings(s):
    vowels, cons = 0, 0
    total_len = len(s)
    for i in range(total_len):
        # Check if the current letter is vowel or consonant
        # Increment the corresponding variable with (total_len - 1)
        # Cause that is the number of substrings you can form
        # starting with the present letter
        # eg. b, ba, ban, bana, banan, banana
        # 6 substrings for b in banana, which is total_len - i = 6 - 0 = 6
        if s[i] in "aeiou":
            vowels += total_len - i
        else:
            cons += total_len - i
    if vowels >= cons:
        return (0, vowels)
    else:
        return (1, cons)

# driver code
input_string = input('Enter String: ')
s = input_string.lower() # convert to lowercase
output = count_substrings(s)
print(output[0], output[1])
