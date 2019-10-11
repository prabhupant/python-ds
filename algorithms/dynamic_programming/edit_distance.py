"""
High Level Description:
Given two words word1 and word2, find the minimum number of operations
required to convert word1 to word2. You have the following 3 operations
permitted on a word:
Insert a character
Delete a character
Replace a character

Time Complexity:
O(m*n)
"""


def edit_dist(str1, str2, m, n):
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]
