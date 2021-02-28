# Minimum swaps required to bring all elements less than or equal to k together

def min_swaps(arr, k):
    # First find out how many elements are there which are less than or 
    # equal to k
    count = 0
    for i in arr:
        if i <= k:
            count += 1

    # This count defines a window - inside this window all our elements should 
    # be placed
    # Find the count of bad elements - elements which are more than k and that will be
    # our starting answer as we will have to swap them out
    bad = 0
    for i in range(0, count):
        if arr[i] > k:
            bad += 1

    ans = bad
    j = count

    for i in range(0, len(arr)):
        if j == len(arr):
            break

        if arr[i] > k:
            bad -= 1  # because we have moved the bad element out of the window
        
        if arr[j] > k:
            bad += 1

        ans = min(bad, ans)
        j += 1

    print('answer - ', ans)

arr = [2,7,9,5,8,7,4]
min_swaps(arr, 5)