'''
Perfect number is a number that if summary
all it's divisors gives you the same number.
'''

def isPerfectNumber(number):
    sum = 0
    for i in range(1,number/2+1):
        if number % i == 0:
            sum += i
    return number == sum

x = isPerfectNumber(6)
if not x:
    print("The number {} isn't perfect number ".format(6))
else:
    print("The number {} is perfect number ".format(6))
