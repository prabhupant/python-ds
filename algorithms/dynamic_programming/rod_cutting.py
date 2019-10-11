'''
Given a rod of length n units and an
array of prices that contains prices
of all pieces of size less than n. We
need to find the maximum maximum price
obtainable by cutting the rod and
selling it.
'''
INT_MIN = -32767


def cutRod(price, n):
    values = [0 for i in range(n+1)]
    values[0] = 0

    for i in range(1, n+1):
        max_value = INT_MIN
        for j in range(i):
            max_value = max(max_value, price[j] + values[i-j-1])
        values[i] = max_value

    return values[n]
