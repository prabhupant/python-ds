"""
Question:
One Away: There are three types of edits that can be performed on
strings: insert a character, remove a character, or replace a
character. Given two strings, write a function to check if they
are one edit (or zero edits) away.

Example:
pale,   ple  -> true
pales,  pale -> true
pale,   bale -> true
pale,   bake -> false

Source: Cracking the Code Interview 6th Edition Question 1.5

Time Complexity:
We are going through both strings at the same time and stopping when
more than one letter is different, which means O(n) time complexity
on the while loop. No extra space is required.
"""

def is_one_away(str1, str2):
    edit_counter = 0
    i = 0 # str1 index
    j = 0 # str2 index

    # Size difference must be less than 1
    if abs(len(str1) - len(str2)) > 1:
        return False

    # Compare strings while counting edits
    # If letters differ, update counter and compare next letter
    # In this case, if strings have different sizes increment only index of the longest
    # Otherwise increment both indexes
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            # Only one edit is allowed
            if edit_counter > 0:
                return False
            edit_counter += 1

            if len(str1) > len(str2):
                i += 1
                continue
            elif len(str1) < len(str2):
                j += 1
                continue
        i += 1
        j += 1

    # If one string finished before the other, we will certainly
    # have one more edit to consider (adding the last letter), so 
    # we must check if the edit counter is still empty
    if (i < len(str1) or j < len(str2)) and edit_counter > 0:
        return False

    return True

# Driver code
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print(is_one_away(str1, str2))
