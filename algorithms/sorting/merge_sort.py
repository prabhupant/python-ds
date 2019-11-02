"""
High level explanation:

merge_sort is a Divide and conquer algorithm that splits in halves the array and
then builds it back up by merging and sorting at the same time its elements.

Time complexity:

merge_sort has a time complexity of O(n log n).
"""

def merge_sort(arr):
    if len(arr) >1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        merge_sort(L) # Sorting the first half
        merge_sort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

test_array = [10,30,20,100,40,80,90,210,34]

merge_sort(test_array)

print(test_array)

# This code is contributed by Mayank Khanna
# and extented by thanasis mpalatsoukas
