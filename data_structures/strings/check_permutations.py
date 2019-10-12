"""
Question:
Check Permutation: Given two strings, write a method to decide if
one is a permutation of the other.
Source: Cracking the Code Interview 6th Edition Question 1.2
"""
from collections import defaultdict


def check_permutations_v1(s1, s2):
    """
    Given two strings checks if one is permutation of the other.

    Time complexity:
    O(n)
    :param s1: str
    :param s2: str
    :return:

    Examples:

    >>> check_permutations_v1("some", "sun")
    False
    >>> check_permutations_v1("sumit", "mtisu")
    True
    >>> check_permutations_v1("geeksforgeeks", "forgeeksgeeks")
    True
    >>> check_permutations_v1("somei", "somee")
    False
    >>> check_permutations_v1("aae", "aaa")
    False

    """
    # Case 1: Not matching length
    if len(s1) != len(s2):
        return False
    # Case 2: Both strings have a length of zero
    if len(s1) == 0 and len(s2) == 0:
        return True
    # Case 3: One Letter Strings
    if len(s1) == 1 and len(s2) == 1:
        return s1[0] == s2[0]
    # Case 4: Length greater than 1 for both strings and lengths are equal
    else:
        # Loop through each char (looping is an O(n) operation)
        counter = {ch: s1.count(ch) for ch in s1}
        for ch in s2:
            # Check if it the ch is in the dictionary (checking is O(1) operation)
            if ch not in counter:
                return False
            counter[ch] -= 1
            if counter[ch] == 0:
                counter.pop(ch)
        return True


def check_permutation_v2(s1, s2):
    """
    Given two strings checks if one is permutation of the other.

    Additional solution by sorting the letters of the words.

    Time complexity: O(n log n)

    :param s1: str
    :param s2: str
    :return:

    Examples:

    >>> check_permutation_v2("some", "sun")
    False
    >>> check_permutation_v2("sumit", "mtisu")
    True
    >>> check_permutation_v2("geeksforgeeks", "forgeeksgeeks")
    True
    >>> check_permutation_v2("somei", "somee")
    False
    >>> check_permutation_v2("aae", "aaa")
    False

    """
    return sorted(s1) == sorted(s2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
