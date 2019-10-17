'''
We are given two sequences and we
need to find the length of the
longest common subsequence
'''


def lcs(S1, S2):
    m = len(S1)
    n = len(S2)

    LCS = [[-1]*(n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCS[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                LCS[i][j] = LCS[i-1][j-1]+1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

    return LCS[m][n]
