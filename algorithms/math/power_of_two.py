"""
	This simple code is to check if a given number is a poer of two or not.
	Method:
		if a number is a power of two, then its binary representation is (2^k).
		ex: 4 --> 2^2 --> 100 --> k = 2
			8 --> 2^3 --> 1000 --> k = 3
			16--> 2^4 --> 10000 --> k = 4
		
		assume that n is a power of two, then (n-1)&(n) will be zero;
		ex:
			n = 8 --> (1000)  , n-1 = 7 ---> (0111)
			performing bit (and) operation between both, then n&(n-1) = 0000
			
			n = 12 --> (1100)  , n-1 = 11 ---> (1011)
			performing bit (and) operation between both, then n&(n-1) = 1000
			
	Conclusion:
		The result of the above bit "and" operation will be zero, ONLY if the given number is a pwoer of two.

	NOTE:
		- Since Python considers 0 as "false", then we are gonna return the inversion of the result; i.e. return not(n&(n-1).
		- BUT If n = 0, the result will be zero indicating that 0 is a power of 2, wich is not true.
			So to fix that, we are going to perform  an extra logical "and" operation with the oreginal number.
"""		
		

def pow_of_two(n):
  return(n and (not(n&(n-1))))

for i in range(20):
  if pow_of_two(i):
    print(f"{i} is a power of 2.")
  else:
    print(f"{i} is NOT a power of 2.")
