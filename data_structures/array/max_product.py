#function for log(a)
i = int(input("please give a number: "))
def power(a,b):
    res = 1
    while(b):
        if(b & 1):
            res = res * a
        a = a * a
        b >>= 1
    return res
#function for max product
def max_product(x):
    if(x == 2):
        return 1
    
    if(x == 3):
        return 2
    
    maxProduct =  0
    if(x % 3 == 0):
        maxProduct = power(3, int(x/3))
        return maxProduct
    elif(x % 3 == 1):
        maxProduct = 2 * 2 * power(3,int(x/3)-1)
        return maxProduct
    elif(x % 3 == 2):
        maxProduct = 2 * power(3,int(x/3))
        return maxProduct
max = max_product(i)
print(max)
