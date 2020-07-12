#Calculate factorial of a given number using recursive method.

def factorial(number):

    if number == 0 or number == 1:
        return 1

    answer = number * factorial(number - 1)

    return answer

if __name__ == '__main__':

    enter_number = int(input("Enter a number whose factorial is required : "))
    result = factorial(enter_number)
    print(result)