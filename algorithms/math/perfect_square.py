def is_perfect_square(num):
    """
    Given a positive integer num, write a function which returns True if num is a perfect square else False.

    Note: Do not use any built-in library function such as `sqrt`.

    :type num: int
    :rtype: bool
    """
    i = 0
    while i * i < num:
        i += 1
    if i * i == num:
        return True
    else:
        return False
        

# Test
print(is_perfect_square(16))
print(is_perfect_square(14))
