import functools

def hamilton_cycle(graph, n):
    height = 1 << n

    dp = [[False for _ in range(n)] for _ in range(height)]
    for i in range(n):
        dp[1 << i][i] = True

    for i in range(height):
        ones, zeros = [], []
        for pos in range(n):
            if (1 << pos) & i:
                ones.append(pos)
            else:
                zeros.append(pos)

        for o in ones:
            if not dp[i][o]:
                continue

            for z in zeros:
                if graph[o][z]:
                    new_val =  i + (1 << z)
                    dp[new_val][z] = True

    return functools.reduce(lambda a, b: a or b, dp[height - 1])