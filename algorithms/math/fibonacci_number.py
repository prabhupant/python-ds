# Program that prints out the numbers of the famous Fibonacci sequence

import sys


def main():
    sequence = initialize_list()
    number = get_input_from_user()
    final_sequence = calculate_sequence(sequence, number)
    print_sequence(final_sequence)
    pass


def initialize_list():
    """
    Initializes a list with that holds the first two Fibonacci numbers.

    :return: a list consisting of 0 and 1, in that order.
    """
    fibonacci_sequence = list()  # initialize an empty list
    fibonacci_sequence.append(0)
    fibonacci_sequence.append(1)
    return fibonacci_sequence


def get_input_from_user():
    """
    Gets a number as input from the user; this numbers states the program as to which point to stop printing out the Fibonacci numbers.

    :return: the number the user entered.
    """
    number = input("Up to which number do you want the program to print the Fibonacci sequence? ")
    return int(number)


def calculate_sequence(sequence: list, number: int):
    """
    Contructs the Fibonacci Sequence up till a certain number in the sequence.

    :param sequence: the initial list holding the Fibonacci numbers.
    :param number: the number at which to stop the Fibonacci sequence.
    :return: a list holding the numbers of the Fibonacci sequence.
    """
    if not number:  # if user entered the number 0
        print("Please enter a valid number!")
        sys.exit(1)  # 'abnormally' exit the program

    while sequence[-1] < number:
        latest_addition = sequence[-2] + sequence[-1]
        sequence.append(latest_addition)
    return sequence


def print_sequence(sequence: list):
    """
    Prints out the Fibonacci numbers that are separated by commas.

    :return: A string representation of the Fibonacci numbers.
    """
    # print([str(i) for i in sequence])  # this prints out the sequence in list format
    print(", ".join(str(i) for i in sequence))


if __name__ == "__main__":
    main()
