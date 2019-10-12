"""
Question :
Given a string consisting of English alphabets, the task is to count the number of adjacent pairs of vowels.
For example :
Input: str = “abaebio”
Output: 2
(a, e) and (i, o) are the only valid pairs.
Source:A very Common Interview Question.

Time Complexity : The goal is to complete this question in O(n).
"""


def is_vowel(char):
    """
    Checks if a char is a vowel.

    :param char:
    :return bool:

    Examples:
    >>> is_vowel("a")
    True
    >>> is_vowel("b")
    False

    """
    return char.lower() in "aeiou"


def adjacent_pairs(s):
    """
    Find the number of adjacent vowel pairs.
    
    :param s: 
    :return:

    Examples:
    >>> adjacent_pairs("almost")
    0
    >>> adjacent_pairs("too")
    1
    >>> adjacent_pairs("tea is tea")
    2
    >>> adjacent_pairs("abaebio")
    2
    """
    s = s.lower()

    return sum((1 if is_vowel(a) and is_vowel(b) else 0 for a, b in zip(s[:-1], s[1:])))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
