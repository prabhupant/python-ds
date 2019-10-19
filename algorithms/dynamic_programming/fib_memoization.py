# this uses dynamic programming specifically memoization
# to reduce the running time for fib sequence

#creating cache
n=998
cache = [None]*(n+1)

def fib(n):

    #base case
    if n<=1:
        return n
    #check cache
    if cache[n]:
        return cache[n]

    #set cache
    cache[n] = fib(n-1)+fib(n-2)
    return cache[n]

print(fib(998))
