"""
Question:
Check Permutation: Given two strings, write a method to decide if
one is a permutation of the other.
Source: Cracking the Code Interview 6th Edition Question 1.2

Time Complexity:
Every letter must be looped which means O(n) time complexity. Then,
we must check if each letter is in the dictionary which is another
O(n) time complexity. Overall, the total time complexity is O(n^2).
"""

letter_counts = {}


def check_permutations(word1, word2):
    # Case 1: Not matching length
    if len(word1) != len(word2):
        return False
    # Case 2: Both strings have a length of zero
    if len(word1) == 0 and len(word2) == 0:
        return True
    # Case 3: One Letter Strings
    if len(word1) == 1 and len(word2) == 1:
        return word1[0] == word2[0]
    # Case 4: Length greater than 1 for both strings and lengths are equal
    else:
        populate_letter_count(word1)
        # Loop through each letter (looping is an O(n) operation)
        for letter in word2:
            # Check if it the letter is in the dictionary (checking is O(n) operation)
            if letter_counts.get(letter) is not None:
                curr_count = letter_counts.get(letter)
                if curr_count == 1:
                    letter_counts.pop(letter)
                else:
                    letter_counts[letter] = curr_count - 1
            else:
                return False
        return True


def populate_letter_count(word1):
    # Loop through each letter (looping is an O(n) operation)
    for letter in word1:
        # Check if it the letter is in the dictionary (checking is O(n) operation)
        if letter_counts.get(letter) is None:
            letter_counts[letter] = 1
        else:
            curr_count = letter_counts.get(letter) + 1
            letter_counts[letter] = curr_count

#########################################################
# additional solution by sorting the letters of the words
def check_permutation2(word1, word2):
    sorted(word1) == sorted(word2)
