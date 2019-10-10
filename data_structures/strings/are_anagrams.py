"""
Question:
Check whether two strings are anagram of each other:
Write a function to check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are anagram of each other.
Source:A very Common Interview Question,asked in companies like Amazon,Goldman Sachs and Nagarro.

Time Complexity:
The goal is to complete this question in O(n).
This solution is optimized by using bit manipulation. If we start at a value of 0 and XOR all the characters of both strings, we should return an end value of 0 if they are anagrams because there would be an even occurrence of all characters in the anagram.

Space Complexity:
The space complexity of this approach is O(1).
"""
# Function to check whether two strings are anagrams of each other  
def are_anagrams(string1, string2): 
      
    # If two strings have different size we return False as they cannot be anagrams of each other
    if (len(string1) != len(string2)): 
        return False
    # Variable to store the Xor Value 
    xor_value = 0
    for i in range(len(string1)):
        xor_value = xor_value ^ ord(string1[i]) 
        xor_value = xor_value ^ ord(string2[i])

    if(xor_value==0):
    	return True
    else:
    	return False

# Code To test The Function
string1 = "thestringsareanagrams"
string2 = "arethestringsanagrams"
if(are_anagrams(string1, string2)): 
    print("The two strings are anagram of each other")
else: 
    print("The two strings are not anagram of each other")


