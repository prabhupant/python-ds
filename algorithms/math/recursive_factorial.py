#Anuneet Anand
# Recursive Factorial
def RF(n):
	if n==1 or n==0:
		return 1
	else:
		return n*f(n-1)

n = int(input())
print(RF)