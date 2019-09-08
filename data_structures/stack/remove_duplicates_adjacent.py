def remove(s):
    stack = []
    for element in s:
        if stack and element == stack[-1]:
            stack.pop()
        else:
            stack.append(element)
    
