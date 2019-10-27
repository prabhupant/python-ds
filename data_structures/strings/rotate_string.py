def is_rotate_string(A, B):
    """
    Given two strings, A and B.

    A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

    :type A: str
    :type B: str
    :rtype: bool
    """
    len_a = len(A)
    len_b = len(B)
    if len_a != len_b:
        return False
    if len_a == 0:
        return True
    for i in range(len_a):
        A = A[-1:] + A[:-1]
        if A == B:
            return True
    return False


# Test
print(is_rotate_string('abcde', 'cdeab'))
print(is_rotate_string('abcde', 'abced'))
