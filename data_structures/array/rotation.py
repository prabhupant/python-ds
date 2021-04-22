def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def rotate(arr, d):
    n = len(arr)
    g = gcd(n, d)

    for i in range(g):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k -= n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
        

arr = [1,2,3,4,5]
rotate(arr, 3)
print(arr)
