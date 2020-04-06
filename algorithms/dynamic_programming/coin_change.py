# Concept is almost same as 01 Knapsack Problem

def min_coin(coins, total):
    cols = total + 1
    rows = len(coins)

    t = [[[0] if col == 0 else float('inf') for col in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(1, cols):
            if j < coins[i]:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = min(t[i-1][j], 1 + t[i][j-coins[i]])

    return t[rows-1][cols-1]
