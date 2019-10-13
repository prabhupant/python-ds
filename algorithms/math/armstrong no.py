# Python program to check if a number is an Armstrong number or not

# input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# the sum of the cube of each digit
temp = num
for n in range(1, temp+1):
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# displaying the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")