"""
High Level Description:
Given two input integers, find their Greatest Common Divisor.

Time Complexity:
O(log(n))
"""
# Iterative Solution


def gcd(x, y):
	if x == 0:
		return y
	if y == 0:
		return x
	
	while x % y != 0:
		rem = x % y
		x = y
		y = rem

	return y


# Recursive Solution
def gcd_rec(x, y):
	if x == 0:
		return y
	if y == 0:
		return x
	
	return gcd(y, x % y)


# TESTING
if __name__ == "__main__":
	assert gcd(360, 84) == 12
	assert gcd_rec(360, 84) == 12
	print("Tests pass.")
