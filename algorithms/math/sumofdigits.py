# This is to find the sum of digits of a number until it is a single digit

def sum_of_digits(n):
    n = int(input()) # here n is the number
    if n % 9 != 0:
        print(n % 9)
    else:
        print("9")
        
# This method reduces time complexity by a factor of n and also without using any loop

