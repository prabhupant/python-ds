# Program that prints out the n given McCarthy 91 number
# Best documentation -> https://en.wikipedia.org/wiki/McCarthy_91_function

def mccarthy_function(number: int) -> int:

    if number > 100:
        return number - 10
    
    return mccarthy_function(mccarthy_function(number + 11))