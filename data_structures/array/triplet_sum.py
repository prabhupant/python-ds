# If space is a constraint, then sort the array first and use two pointer
# solution. In that case, the time complexity will be O(n^2 + nlogn)


def find_hash(arr, sum):
    
    for i in range(0, len(arr) - 1):
        s = set()
        current_sum = sum - arr[i]
        for j in range(i+1, len(arr)):
            if (current_sum - arr[j]) in s:
                return "Values are {}, {}, {}".format(arr[i], arr[j], current_sum-arr[j])
            s.add(arr[j])
    return "Not found"

arr = [1,2,3,4,5,6,7,8,9]

print(find_hash(arr, 14))
