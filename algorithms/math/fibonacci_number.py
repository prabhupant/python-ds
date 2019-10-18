# Program that prints out the fibonacci sequence until a given number

# def calc_fib(num):
#     while len(fib) <= num:
#         n = len(fib)
#         fib.append((fib[n-1] + fib[n-2]))
        
# def main():
#     print("Enter the Position of the Number in the Sequence or \'0\' to Quit: ")
#     num = 0
#     fib = list()
#     fib.append(0)
#     fib.append(1)

#     while True:
#         num = int(input())
#         if(num <= 0):
#             break

#         if len(fib) <= num:
#             calc_fib(num)

#         print('Fibonacci Number at Position ' + str(num) + ' is: ' + str(fib[num]))
        
# if __name__ == '__main__':
#     main()


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
        sys.exit(1)
    while sequence[-1] < number:
        latest_addition = sequence[-2] + sequence[-1]
        sequence.append(latest_addition)
    return sequence


def print_sequence(sequence: list):
    """
    Prints out the Fibonacci numbers that are separated by commas.

    :return: A string representation of the Fibonacci numbers.
    """
    for i in sequence:
        # print(", ".join(sequence))  # this will most likely not end up to what I want it to be
        print(i, end=", ")


if __name__ == "__main__":
    main()
