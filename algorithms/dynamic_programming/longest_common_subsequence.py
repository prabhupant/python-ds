def lcs(str1, str2):
    """
    We are given two sequences and we
    need to find the length of the
    longest common sub-sequence.

    :param str1:
    :param str2:
    :return int: longest common sub-sequence

    Examples:

    >>> lcs("AGGTAB", "GXTXAYB")
    4

    """
    m = len(str1)
    n = len(str2)

    lcs_dp = [[-1] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                lcs_dp[i][j] = lcs_dp[i - 1][j - 1] + 1
            else:
                lcs_dp[i][j] = max(lcs_dp[i - 1][j], lcs_dp[i][j - 1])

    return lcs_dp[m][n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
