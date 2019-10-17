'''
Question :
Given a string consisting of English alphabets, the task is to count the alphabets in the longest palindromic subsequence.

For example :
Input: str = "BBABCBCAB"
Output:  7 
"BABCBAB" is the longest palindromic subseuqnce in it. "BBBBB"" and "BBCBB" are also palindromic subsequences of the given sequence, but not the longest ones.

Source: https://www.geeksforgeeks.org/python-program-for-longest-palindromic-subsequence-dp-12/
'''

def lps(str): 
    n = len(str) 
  
    # Create a table to store results of subproblems 
    L = [[0 for x in range(n)] for x in range(n)] 
  
    # Strings of length 1 are palindrome of length 1 
    for i in range(n): 
        L[i][i] = 1
  
    # Build the table. Note that the lower  
    # diagonal values of table are 
    # useless and not filled in the process.  
    for cl in range(2, n + 1): 
        for i in range(n-cl + 1): 
            j = i + cl-1
            if str[i] == str[j] and cl == 2: 
                L[i][j] = 2
            elif str[i] == str[j]: 
                L[i][j] = L[i + 1][j-1] + 2
            else: 
                L[i][j] = max(L[i][j-1], L[i + 1][j]); 
  
    return L[0][n-1] 
  
# Test inputs
seq = "BBABCBCAB"
print("The length of the LPS is " + str(lps(seq)))
