#  Find all the pairs of two integers in an unsorted array that sum up to a given S. 

# our two sum function which will return
# all pairs in the list that sum up to S
def twoSum(arr, S):

  sums = []

  # check each element in array
  for i in range(0, len(arr)):

    # check each other element in the array
    for j in range(i+1, len(arr)):

      # determine if these two elements sum to S
      if (arr[i] + arr[j] == S):
        sums.append([arr[i], arr[j]])

  # return all pairs of integers that sum to S
  return sums

print twoSum([3, 5, 2, -4, 8, 11], 7)  
