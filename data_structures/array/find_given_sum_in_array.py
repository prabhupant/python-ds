# Find if a given sum exists in an array
# Reference - https://www.geeksforgeeks.org/find-subarray-with-given-sum/

def find_sum(arr, s):
    curr_sum = arr[0]
    start = 0
    n = len(arr) - 1
    
    i = 1

    while i <= n:
        
        while curr_sum > s and start < i:
            curr_sum = curr_sum - arr[start]
            start += 1

        if curr_sum == s:
            return "Found between {} and {}".format(start, i - 1)

        curr_sum = curr_sum + arr[i]
        i += 1

    return "Sum not found"

arr = [15, 2, 4, 8, 9, 5, 10, 23] 

print(find_sum(arr, 6))
