'''
This program takes as an input the coins that need be
converted to the minimum amount of real currency in coins.
The program is classified as an greedy algorithm because
it takes always the maximum value of real currency to
reach the amount specified.
'''

def coinChanges(centsChanges):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    z = []
    while centsChanges != 0:
        for coin in coins:
            if centsChanges - coin >= 0:
                centsChanges -= coin
                z.append(coin)
                break
    return z

y = coinChanges(834) # The number 834 is the amount of cents we want to get as changes
print(y)
