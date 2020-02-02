def knapsack(values, weights, total):
    total_items = len(weights)

    rows = total_items + 1
    cols = total + 1

    # rows are the number of items
    # columns are the values of weights required

    t = [[0 for i in range(cols)] for i in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if j < weights[i-1]:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = max(t[i-1][j], values[i-1] + t[i-1][j-weights[i-1]])

    return t[rows-1][cols-1]


weights = [1,3,4,5]
values = [1,4,5,7]

ans = knapsack(values, weights, 7)
print(ans)
