def check(s):
    stack = []
    for element in s:
        if element == '(':
            stack.append(')')
        elif element == '[':
            stack.append(']')
        elif element == '{':
            stack.append('}')
        elif not stack or stack.pop() != element:
            return False
    return not stack
