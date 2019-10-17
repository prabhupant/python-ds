'''
Question:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M and their values are 1,5,10,50,100,500,1000 respectively.Given a roman numeral,convert it to an integer.Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input : 'XI'
Output : 11

Example 2:
Input : 'CCCXL'
Output : 340

Source: Interview question.

Time Complexity : O(n)
Space Complexity : O(1)

'''

# Function to convert a roman numeral to an integer
def roman_to_integer(input):
    romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    sum=0
    for i in range(input):
        # Getting the value of the symbol
        value=romans[input[i]]
        # Comparing if the next value is bigger or smaller than the current value
        if i+1<len(input):
            if romans[input[i+1]]>value:
                # If it is big, the value is subtracted from the sum
                sum-=value
        else:
            sum+=value
    return sum

# Main code
print("Roman to integer conversion of")
input=input.upper()
roman_to_integer(input)

