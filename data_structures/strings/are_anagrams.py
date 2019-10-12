"""
Question:
Check whether two strings are anagram of each other:
Write a function to check whether two given strings are anagram of each other or not.
An anagram of a string is another string that contains same characters, only the order
of characters can be different. For example, “abcd” and “dabc” are anagram of each other.
Source:A very Common Interview Question,asked in companies like Amazon,Goldman Sachs and Nagarro.

Time Complexity:
The goal is to complete this question in O(n).
This solution is optimized by using bit manipulation.
If we start at a value of 0 and XOR all the characters of both strings,
we should return an end value of 0 if they are anagrams because there would be
an even occurrence of all characters in the anagram.

Space Complexity:
The space complexity of this approach is O(1).
"""


def anagrams(s1, s2):
    """
    Checks whether two strings are anagrams of each other.
    :param s1:
    :param s2:
    :return:

    Examples:
    >>> anagrams("sun", "some")
    False
    >>> anagrams("act", "cat")
    True
    >>> anagrams("ward", "draw")
    True
    >>> anagrams("markers", "remarks")
    True
    >>> anagrams("ray", "rye")
    False
    """
    # If two strings have different size we return False as they cannot be anagrams of each other
    if len(s1) != len(s2):
        return False
    # Variable to store the Xor Value 
    xor_value = 0
    for a, b in zip(s1, s2):
        xor_value = xor_value ^ ord(a)
        xor_value = xor_value ^ ord(b)

    return xor_value == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
