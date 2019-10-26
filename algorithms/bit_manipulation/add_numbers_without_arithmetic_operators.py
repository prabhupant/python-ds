# Program to add two numbers without using arithmetic operators

def add(x,y):
    while y != 0:
        carry = (x & y)
        x = (x ^ y)
        y = carry << 1

    return x

# The logic is similar to expressions derived from adding two numbers using a half adder

