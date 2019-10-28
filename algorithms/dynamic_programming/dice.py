'''
Given n dices each with m faces, numbered from 1 to m,
find the number of ways to get a given sum X.
X is the summation of values on each face when all the dice are thrown.

'''

dp = [[-1 for i in range(x+1)] for j in range(n+1)]


def num_of_ways(m, n, x):
    if x == 0 and n == 0:
        return 1
    if x < 0 or n == 0:
        return 0
    if dp[n][x] != -1:
        return dp[n][x]

    ans = 0
    for i in range(1, m + 1):
        ans += num_of_ways(m, n - 1, x - i)

    dp[n][x] = ans
    return ans
