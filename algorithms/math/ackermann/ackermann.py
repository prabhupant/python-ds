# Program that prints out the n given ackerman number
# Best documentation -> https://en.wikipedia.org/wiki/Ackermann_function

def ackermann_function (inferior_limit: int, superior_limit: int) -> int:
    if inferior_limit == 0:
        return superior_limit + 1

    elif superior_limit == 0:
        return ackermann_function(inferior_limit - 1, 1)
    
    return  ackermann_function(inferior_limit - 1, ackermann_function(inferior_limit, superior_limit - 1))
