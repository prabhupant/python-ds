def calc_fib(num):
    while len(fib)<=num:
        n = len(fib)
        fib.append((fib[n-1]+fib[n-2]))
        
def main():
    print("Enter the Position of the Number in the Sequence or \'0\' to Quit: ")
    num = 0
    fib = list()
    fib.append(0)
    fib.append(1)
    while True:
        num = int(input())
        if(num<=0):
            break

        if len(fib)<=num:
            calc_fib(num)

        print('Fibonacci Number at Position '+str(num)+' is: '+str(fib[num]))
        
if __name__ == '__main__':
    main()
