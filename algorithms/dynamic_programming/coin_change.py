
def min_coins(coins, total):
    cols = total + 1

    min_coins = [float('inf')] * (total + 1)
    coins_used = [-1] * (total + 1)

    min_coins[0] = 0  # to form 0, we need 0 coins

    for i in range(0, len(coins)):
        for j in range(1, len(min_coins)):
            if coins[i] > j:  # if the coin value is more than j (curr total), ignore it
                continue

            if (1 + min_coins[j - coins[i]]) < min_coins[j]:
                min_coins[j] = 1 + min_coins[j - coins[i]]
                coins_used[j] = i

    # finding which coins were used
    picked_coins = []
    while total > 0:
        index_of_coin_used = coins_used[total]
        coin = coins[index_of_coin_used]
        picked_coins.append(coin)
        total -= coin

    print('Min coins needed - ', min_coins[-1])
    print('Coins used - ', picked_coins)

total = 11
coins = [9, 6, 5, 1]

min_coins(coins, total)
