# Program that prints out the n given factorial number

def factorial_iterative (number: int) -> int:

    factorial_number = 1

    for iterator in range(1, number + 1):
        factorial_number *= iterator
    
    return factorial_number
