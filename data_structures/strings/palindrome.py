#string question
#to check if a string is a palindrome or not
#python3

s=input("enter the string)
r=s[::-1] #finding reverse string
if r==s:
    print(s,"is a palindrome")
else:
    print (s,"is not a palindrome")
