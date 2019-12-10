'''
Question: Given three strings A, B and C. Write a function that checks whether C 
is an interleaving of A and B. C is said to be interleaving A and B, if 
it contains all characters of A and B and order of all characters in 
individual strings is preserved.

Solution: We include one character from String A or String B and check whether the resultant 
string formed so far by one particular interleaving of the the current prefix of String A 
and String B form a prefix of String C. This can be achieved using dynamic programming.
This approach relies on fact that in order to determine whether a 
substring of String C(upto index k), can be formed by interleaving strings String A 
and String B upto indices i and j respectively depends on the characters of 
String A and String B upto indices i and j only and not on characters coming afterwards.

Complexity analysis -
Time complexity : O(m x n) . dp array of size n is filled m times where m and n are lengths of 
String A and String B respectively.
Space complexity : O(n)

'''

#Function to check if String C is formed by interleaving of String A and B
#Returns a boolean value
def isInterleaving(string_A, string_B, string_C):
    #Check if the length of String C is equal to sum of lengths of String A and B
    #In other words, check if String C contains all characters of String A and B
    if(len(string_C) != len(string_A) + len(string_B)): return False
    
    #Create an empty array of length of String B
    dp = [None] * (len(string_B) + 1)
    
    for i in range(len(string_A) + 1):
        for j in range(len(string_B) + 1):
            if(i == 0 and j == 0):
                #The first value of array dp always holds True
                dp[j] = True
            elif(i == 0):
                dp[j] = dp[j - 1] and string_B[j - 1] == string_C[j - 1]
            elif(j == 0):
                dp[j] = dp[j] and string_A[i - 1] == string_C[i - 1]
            else:
                dp[j] = ((dp[j] and string_A[i - 1] == string_C[i + j - 1]) or (dp[j - 1] and string_B[j - 1] == string_C[i + j - 1]))
	
    	
    return dp[len(string_B)]

#Driver Code
string_A = input("Enter string A")
string_B = input("Enter string B")
string_C = input("Enter string C")

result = isInterleaving(string_A, string_B, string_C)

if(result):
	print("String C is interleaving String A and String B")
else:
	print("String C is not interleaving String A and String B")