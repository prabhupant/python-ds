# min coins required to make a target example
# you have coins of value 1,5,10,25 and target is 74 then you have to fund min no of coins required to reach the target value
#  in this case ans is 8 ie 2(val=25)+2(val=10)+4(val=1)
# memoization is used in this to reduce the time complexity

def minCoin(coins,target,knownres):
    #default value for output
    min_coins=target
    #base case
    if target in coins:
        knownres[target]=1
        return 1

    #return known result if its greater than 0
    elif knownres[target]>0:
            return knownres[target]
    # loop over coins with lesser value than target
    else:
        for i in [c for c in coins if c<=target]:
            # recursively reduce the target( as i value coin has reduced the target ) 
            numcoins = 1+minCoin(coins,target-i,knownres)
            # if the new combination requires less coins then assign min_coins = numcoins
            if numcoins<min_coins:
                min_coins = numcoins
            knownres[target] =  min_coins
    return min_coins

target =74
knownres=[0]*(target+1)
coins = [1,5,10,25]

print(minCoin(coins,target,knownres))
