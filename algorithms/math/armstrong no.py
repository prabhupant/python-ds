 Python program to check if a number is an Armstrong number or not

# input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# displaying the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")