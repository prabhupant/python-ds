# Question: Calculate the sum of two integers a and b but without the
# 			use of the operators + and -.

#Solution
def getSum(a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        mask = 0xffffffff
        diff = 0
        carry = 0
        while b & mask:
            diff = a ^ b
            carry = trunc(a & b)
            carry = carry << 1
            a = diff
            b = carry
        if b > 0: return (a & mask)
        else: return a