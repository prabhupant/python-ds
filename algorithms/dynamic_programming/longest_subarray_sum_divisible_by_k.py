"""
Find the longest subarray in an array whose sum is `
divisible by k

source - https://www.geeksforgeeks.org/longest-subarray-sum-divisible-k/

The idea is that we create a new array mod_arr where we mod_arr[i] = 
sum(arr[0]...arr[i]) % k. So basically this array tells us that upto this
point in the input array, if we take sum of numbers till index i, that sum will
be divisible by k

We will be creating a hash table for this to store the mod results

Now, lets say x = sum(arr[0]...arr[i]) % k = mod_arr[i]. If

1. if we find x == 0, increment length by 1
2. if x not in hash, create it and store (x, index of x)
3. if x in hash:
    this tells us that upto this point, where the remainder of sum of numbers
    till this point divided by k is x, that remainder we already saw before as it 
    exists in the hash. So if we ignore the first dont consider the first occurence of x
    and remove that from the sum, then this sum will be divisible by k (because subtracting remainder
    from a number makes it divisible).
    Now find the max length of such case as 
    if length = max(length, (i - index(x))
"""

def find_length(arr, k):
    hash_table = {}
    mod_arr = []
    s = 0
    length = 0
    start, end = 0, 0

    for i in range(0, len(arr)):
        s += arr[i]
        mod_arr.append(s % k)

    for i in range(0, len(mod_arr)):
        if mod_arr[i] == 0:
            length += 1
        else:
            if mod_arr[i] not in hash_table:
                hash_table[mod_arr[i]] = i
            else:
                if length < (i - mod_arr[i]):
                    length = i - mod_arr[i]
                    start = mod_arr[i]
                    end = i - 1 # i-1 because the current number is not to considered as it makes the sum not divisible by k
    
    return length, arr[start:end+1]


arr = [ 2, 7, 6, 1, 4, 5 ]
print(find_length(arr, 3))
