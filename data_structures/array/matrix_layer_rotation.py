"""
Description:

Matrix Layer Rotation

You are given a 2D matrix of dimension mxn and a positive integer r. You have to rotate the
matrix r times and print the resultant matrix. Rotation should be in anti-clockwise direction.
Rotation of a 4x5 matrix is represented by the following figure. Note that in one rotation,
you have to shift elements by one step only. This is shifting the elemment.
Note:- Minimum of m and n will be even.

Start         First           Second
 1 2 3 4        2  3  4  5      3  4  5  6
12 1 2 5  ->   1  2  3  6 ->   2  3  4  7
11 4 3 6      12  1  4  7       1  2  1  8
10 9 8 7      11 10  9  8     12 11 10  9
"""


# Function to rotate the sides of the matrix in place.
def matrix_rotate(matrix, m, n, i=0, j=0):
    if (m, n) == (1, 1):
        return matrix
    if (m, n) == (2, 2):
        temp = matrix[i][j]
        matrix[i][j] = matrix[i + 1][j]
        matrix[i + 1][j] = matrix[i + 1][j + 1]
        matrix[i + 1][j + 1] = matrix[i + 1][j]
        matrix[i + 1][j] = temp
        return matrix
    else:
        temp = matrix[i][j]
        # top
        for a in range(j, n - j - 1):
            matrix[i][a] = matrix[i][a + 1]
        matrix[i][n - j - 1] = matrix[i + 1][n - j - 1]
        # right
        for a in range(i + 1, m - i - 2):
            matrix[a][n - 1 - j] = matrix[a + 1][n - 1 - j]
        matrix[m - j - 2][n - j - 1] = matrix[m - j - 1][n - j - 1]
        # bottom
        for a in range(n - j - 1, j, -1):
            matrix[m - j - 1][a] = matrix[m - j - 1][a - 1]
        matrix[m - j - 1][j] = matrix[m - j - 2][j]
        # left
        for a in range(m - i - 2, i, -1):
            matrix[a][i] = matrix[a - 1][i]
        matrix[i + 1][j] = temp
        return matrix


def driver_code(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    i, j = 0, 0
    s = 0
    while (i, j) < (m // 2, n // 2):  # Checking for the maximum values of i, j.
        for _ in range(r):
            s = matrix_rotate(matrix, m, n, i, j)
        i += 1
        j += 1
    print_matrix(s)


def print_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    print('\n'.join([' '.join(['{:n}'.format(item) for item in row])
                     for row in matrix]))


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix2d = []

    for _ in range(m):
        matrix2d.append(list(map(int, input().rstrip().split())))

    driver_code(matrix2d, r)


