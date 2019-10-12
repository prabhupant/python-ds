def edit_dist(str1, str2):
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

    :param str1: first string
    :param str2: second string
    :return: min number of operations

    Examples:

    >>> edit_dist("geek", "gesek")
    1
    >>> edit_dist("cat", "cut")
    1
    >>> edit_dist("sunday", "saturday")
    3

    """
    m = len(str1)
    n = len(str2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
