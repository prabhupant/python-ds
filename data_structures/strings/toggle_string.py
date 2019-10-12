"""
Question
You have been given a String S consisting of uppercase and lowercase English alphabets.
You need to change the case of each alphabet
in this String. That is, all the uppercase letters should be converted to lowercase
and all the lowercase letters should be converted
to uppercase. You need to then print the resultant String to output.
Source Hackerearth

SAMPLE INPUT 
abcdE
SAMPLE OUTPUT 
ABCDe
"""


def toggle_string_v1(s):
    """
    Toggles string case.
    :param s:
    :return:

    Examples:

    >>> toggle_string_v1("abcdE")
    'ABCDe'
    >>> toggle_string_v1("ABCDe")
    'abcdE'
    >>> toggle_string_v1(toggle_string_v1("ABCDe"))
    'ABCDe'

    """
    return s.swapcase()


def toggle_string_v2(s):
    """
    Toggles string case.
    :param s:
    :return:

    Examples:

    >>> toggle_string_v2("abcdE")
    'ABCDe'
    >>> toggle_string_v2("ABCDe")
    'abcdE'
    >>> toggle_string_v2(toggle_string_v2("ABCDe"))
    'ABCDe'

    """
    return "".join((ch.lower() if ch.isupper() else ch.upper() for ch in s))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
