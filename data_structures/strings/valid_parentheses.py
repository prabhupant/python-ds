def is_valid_parentheses(s):
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

    :type s: str
    :rtype: bool
    """
    m = {')':'(', ']':'[', '}':'{'}
    stack = []
    for c in s:
        if c not in m:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            elif m[c] != stack.pop():
                return False
    return len(stack) == 0

# Test
print(is_valid_parentheses('()[]{}'))
print(is_valid_parentheses('([)]'))
print(is_valid_parentheses('{[]}'))
