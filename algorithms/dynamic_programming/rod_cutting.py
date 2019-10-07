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

arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))
