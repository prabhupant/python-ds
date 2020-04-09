# Program that prints out the n given factorial number

def factorial_recursive(number: int) -> int:
    
    if number == 0 or number == 1:
        return 1
    else:
        return  number * factorial_recursive(number - 1)