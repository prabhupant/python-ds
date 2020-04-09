# Program that prints out the n given catalan number
# Best documentation -> https://en.wikipedia.org/wiki/Catalan_number

def catalan_function (number: int) -> int:

    if number <= 1:
        return 1

    rest = 0

    for iterator in range(number):
        rest += catalan_function(iterator) * catalan_function(number - iterator - 1)

    return rest
