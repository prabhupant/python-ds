"""
Find the longest subarray in the input array such that the pairwise sum of 
the elements of this subarray is not divisible by K

The idea is -
How can we tell that two numbers x and y will make a pairsum that will be
divisible by K just by looking at their remainders? There can be two conditions

1. It will be only possible if the sum of the remainders when x and y are
divided by K is equal to K. As the sum of the remainders cannot exceed K
so if it reaches K then it means that the sum of those numbers will also be
divisible by K
0 < (X%K) + (Y%K) <= K

2. If arr[i] %  k == 0 and there is also an element j such that arr[j] % k == 0
and 0 exists in the hash (i.e hash[j] = True)
"""

def find_subarray(arr, k):
    """
    True means divisible by k
    """
    start, end = 0, 0
    max_start, max_end = 0, 0

    n = len(arr)
    mod_arr = [0] * n

    mod_arr[arr[0] % k] = mod_arr[arr[0] % k] + 1

    for i in range(1, n):
        mod = arr[i] % k

        while (mod_arr[k - mod] != 0) or (mod == 0 and mod_arr[mod] != 0):
            mod_arr[arr[start] % k] = mod_arr[arr[start] % k] - 1
            start += 1

        mod_arr[mod] = mod_arr[mod] + 1
        end += 1

        if (end - start) > (max_end - max_start):
            max_end = end
            max_start = start

    print(f'Max size is {max_end - max_start}')

    for i in (max_start, max_end + 1):
        print(arr[i], end=" ")


arr = [3, 7, 1, 9, 2]
k = 3
find_subarray(arr, k)

