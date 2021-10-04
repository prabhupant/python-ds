"""
Find the min cost of tiles to cover a floor. 
Floor is represented by 2D array where -
* = tile already placed
. = no tile

tiles available are 1*1 and 1*2 and their costs
are A and B

Source - https://www.geeksforgeeks.org/minimize-cost-to-cover-floor-using-tiles-of-dimensions-11-and-12/
"""

def cost(arr, A, B):
    n = len(arr)
    m = len(arr[0])

    ans = 0

    for i in range(n):
        j = 0
        
        while j < m:
            if arr[i][j] == '*':  # tile is already there
                j += 1
                continue

            if j == m - 1:  # if j is pointing to last tile, you can use only 1*1 tile
                ans += A
            else:
                if arr[i][j+1] == '.':
                    ans += min(2 * A, B)
                    j += 1
                else:
                    ans += A

            j += 1

    print('Cost of tiling is - ', ans)

arr = [ [ '.', '.', '*' ],
        [ '.', '*', '*' ] ]

A, B = 2, 10

cost(arr, A, B)
