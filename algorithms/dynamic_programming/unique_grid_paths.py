"""
High Level Description:
A preson is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below). The preson can only move either down or right at any point
in time. The preson is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).
How many possible unique paths are there?

Time Complexity:
O(m*n)
"""


def number_of_paths(m, n):
    count = [[0 for x in range(m)] for y in range(n)]

    for i in range(m):
        count[i][0] = 1

    for j in range(n):
        count[0][j] = 1

    for i in range(1, m):
        for j in range(n):
            count[i][j] = count[i-1][j] + count[i][j-1]
    return count[m-1][n-1]
