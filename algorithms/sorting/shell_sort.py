'''
Time complexity of shell_sort is O(n2).
In the above implementation gap is reduce by half in every iteration.
here are many other ways to reduce gap which lead to better time complexity.
See this for more details.
'''

def shell_sort(arr):

    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = int(n / 2)

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap = int(gap / 2)

arr = [ 12, 34, 54, 2, 3]

shell_sort(arr)
print(arr)