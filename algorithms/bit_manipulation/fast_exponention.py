# Fastest Exponention using Bit Manipulation.

'''
Convert the integer n into binary form and follow the steps below: 

1.Initialize result with 1 to store   a^n.

2.Traverse until n > 0 and in each iteration, perform Right Shift operation on it.

3.Also, in each iteration, multiply a with itself and update it.

4.If current LSB is set, then multiply current value of a to result.

5.Finally, after completing the above steps, print result.

'''
def fastExponention(a, n):
    result = 1
    while (n > 0): 
        last_bit = (n & 1)
        # Check if current LSB  
        # is set  
        if (last_bit):  
            result = result * a 
        a = a * a 
        # Right shift  
        n = n >> 1
    return result
if __name__ == '__main__': 
    a = int(input("enter the value of base:"))
    n = int(input("enter the value of exponent:"))
    print(fastExponention(a,n)) 
    
    
  
