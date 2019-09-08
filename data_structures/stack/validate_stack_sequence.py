# pushed = [1,2,3,4,5]
# popped = [4,5,3,2,1]

# this sequence is possible

def verify(pushed, popped):
    i = 0
    stack = []
    for x in pushed:
        stack.append(x)
        while stack and i < len(popped) and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return i == len(popped)
