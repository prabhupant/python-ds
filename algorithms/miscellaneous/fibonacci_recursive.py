# Basic showcase of recursion using fibonacci series

def rec_fibo(n):
   if n <= 1:
       return n
   else:
       return(rec_fibo(n-1) + rec_fibo(n-2))

loops = int(input("How many loops? "))

if loops <= 0:
   print("Plese enter a positive integer")
else:
   for i in range(loops):
       print(rec_fibo(i))