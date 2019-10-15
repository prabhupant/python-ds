# "Given a number , write a program to reverse this number using stack."


# The idea to do this is to extract digits of the number and push the digits on to a stack. Once all of the digits of the       number are pushed to the stack, we will start poping the contents of stack one by one and form a number.
#As stack is a LIFO data structure, digits of the newly formed number will be in reverse order.




st = [];                                               # stack created using a List Data Structure.

# Function to push digits into stack 
def push_digits(number): 

	while (number != 0): 
		st.append(number % 10)                         # extraction of digit from number and appending into stack
		number = int(number / 10)                      #reducing the number by 1 digit from the end                                 

# Function to reverse the number 
def reverse_number(number): 
	
	# Function call to push number's 
	# digits to stack 
	push_digits(number)
	
    reverse = 0
	i = 1
	
	# Popping the digits and forming 
	# the reversed number 
	while (len(st) > 0): 
		reverse = reverse + (st[len(st) - 1] * i)
		st.pop() 
		i = i * 10 
	
	# Return the reversed number formed 
	return reverse 

# Driver Code 
number = int.input()

# Function call to reverse number 
print(reverse_number(number))


