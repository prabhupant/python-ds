"""
Bucket sort or bin sort is useful when sorting values
inside a range that values are uniformly distributed,
it consists in distributing the elements into a number
of buckets and then sortingthem individually using any
sorting algorithm. Given a uniformly distributed input bucket sort
runs in O(n) in the average-case.
"""


# The slot input means the number os slots
def bucket_Sort(x, n_slots=10):
    arr = [[] for x in range(n_slots)]
    n = 0

    # Put array elements in different buckets
    for h in x:
        index = int(n_slots * h)
        arr[index].append(h)

    # Sort the buckets and concatenate them
    for i in range(n_slots):
        arr[i] = Sort(arr[i])
        for j in arr[i]:
            x[n] = j
            n += 1
    return x


def Sort(arr):
    for i in range(1, len(arr)):
        it = arr[i]
        x = i - 1
        while x >= 0 and arr[x] > it:
            arr[x + 1] = arr[x]
            x -= 1
        arr[x + 1] = it
    return arr

# Test the Bucket Sort
# x = [0.6234, 0.423, 0.3234, 0.13442, 0.265,
#    0.5435, 0.743, 0.8423, 0.9324, 0.9532, 0.96243]
# print(bucket_Sort(x))
