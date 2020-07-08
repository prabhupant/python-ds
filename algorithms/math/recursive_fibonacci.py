"""
    Recursivly compute the Fibonacci sequence using two different methods
    main() compares the amount of time taken by each algorithm
    rec_fib(n) requires O(Fibo(n)) operations, whereas binary_rec_fib(n) requires less than O(n) 
"""

import time

def rec_fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return rec_fib(n-1)+rec_fib(n-2)

def binary_rec_fib(n):
    if n == 2 or n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        sgn = n % 2
        return binary_rec_fib((n-sgn)/2+1)**2 - ((-1)**sgn)*binary_rec_fib((n+sgn)/2-1)**2

def main():
    times = []
    n : int = int(input("n := "))
    for i in range(0,n):
        print(binary_rec_fib(i))

if __name__ == "__main__":
    main()
