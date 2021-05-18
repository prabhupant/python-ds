stack = []
def checkBalanced(expr):
    for i in expr:
        if i == "{" or i == "[" or i == "(":
            stack.append(i)
        elif i == "}" or i == "]" or i == ")":
            if not stack:
                return False
            top = stack.pop()
            if i == "}" and top != "{":
                return False
            elif i == "]" and top != "[":
                return False
            elif i == ")" and top != "(":
                return False
        else:
            print("Invalid Expression")
            return False

    if not len(stack):
        return True
    else:
        return False

# main function
expr = input()
if not checkBalanced(expr):
    print("Not Balanced")
else:
    print('Balanced')
