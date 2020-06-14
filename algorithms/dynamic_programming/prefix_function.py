
def prefix_function(s: str) -> [int]:
    """
    The prefix function for string s is defined as an array pi of length n,
    where pi[i] is the length of the longest proper prefix of the substring
    s[0...i] which is also a suffix of this substring. A proper prefix of a
    string is a prefix that is not equal to the string itself.
    By definition, pi[0] = 0.
    """
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while (j > 0) and (s[i] != s[j]):
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi
