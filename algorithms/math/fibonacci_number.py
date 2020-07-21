# Program that prints out the fibonacci sequence until a given number


def main():
    n = int(input("insert number: "))
    fib = [1, 1]
    for i in range(2, n, 1):
        fib.append(fib[i-1] + fib[i-2])

    print("The first", str(n), "Fibonacci numbers are:", fib)


if __name__ == '__main__':
    main()
