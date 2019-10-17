"""
    Recursivly compute the Fibonacci sequence
"""

def rec_fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return rec_fib(n-1)+rec_fib(n-2)

def main():
    n : int = int(input("n := "))
    for i in range(0, n):
        print(rec_fib(i))

if __name__ == "__main__":
    main()
