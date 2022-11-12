"""
Prefix sum algorithm
Complexity = O(N)
Return array of sums from the queries list.
For example, if the numbers is [1,2,3,4,5] and queries is [[0,1],[2,3],[4,5]].
The first element in the queries list(queries[0]) should return summation of elements
from index 0 to 1 in array numbers.
"""

def prefix_sum(numbers, queries):
    prefix = []
    output = []
    prefix.append(numbers[0])
    numbers_index = 1
    while numbers_index < len(numbers):
        prefix.append(prefix[numbers_index-1] + numbers[numbers_index])
        numbers_index += 1
    queries_index = 0
    while queries_index < len(queries):
        if queries[queries_index][0] == 0:
            output.append(prefix[queries[queries_index][1]])
        else:
            output.append(prefix[queries[queries_index][1]] - prefix[queries[queries_index][0]-1])
        queries_index += 1
    return output

"""
test cases
"""
print(prefix_sum([3, 0, -2, 6, -3, 2], [[0, 2], [2, 5], [0, 5]]))
print(prefix_sum([-1000], [[0, 0]]))
print(prefix_sum([34, 19, 21, 5, 1, 10, 26, 46, 33, 10], [[3, 7], [3, 4], [3, 7], [4, 5], [0, 5]]))
print(prefix_sum([-4, -18, -22, -14, -33, -47, -29, -35, -50, -19],
                 [[2, 9], [5, 6], [1, 2], [2, 2], [4, 5]]))