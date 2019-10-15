"""
Find Nth prime number
"""
import math

"""
Checks if a given number is prime or not
params:
    num: (int)
returns: (boolean) True or False depending upon whether the given number is prime or not
"""
def is_prime(num):
    if num%2 == 0:
        return False
    else:
        i = 3
        num_sqrt = math.sqrt(num)
        # Checking divisibility till square root of the given number
        while i <= num_sqrt:
            if num%i == 0:
                return False
            i += 2
        return True


"""
Calculates Nth prime number
params:
    num: (int)
returns: (int) Nth prime number
"""
def nth_prime_number(num):
    if num < 1:
        return -1
    if num == 1:
        return 2
    curr_prime_count = 1
    temp = 1
    while curr_prime_count < num:
        temp += 2
        while not is_prime(temp):
            # Incrementing number by 2 as we can skip even numbers for prime check
            temp += 2
        curr_prime_count += 1
    return temp


print(nth_prime_number(20))
