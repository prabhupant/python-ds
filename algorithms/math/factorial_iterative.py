#Calculate factorial of a given number using iterative method.

def factorial(number):

    answer = 1

    if number == 0:
        return 1
    else:
        for num in range(1, number+1):
            answer = answer * num
    return answer

if __name__ == '__main__':

    enter_number = int(input("Enter a number whose factorial is required : "))
    result = factorial(enter_number)
    print(result)