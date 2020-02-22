'''
Time Complexity of Gnome Sort is : O(N^2)
Gnome Sort is a simple sorting algorithm where the key idea is to swap adjacent elements
(if not in order) to sort the entire list. It is similar to Insertion sort except the fact
that in this case, we swap adjacent elements.

'''
def gnome_Sort(arr): 
        # Setting the index value to 0
        index = 0
        # Calculating Length of an Array.
        n = len(arr)
        # Code Logic
        while index < n: 
            if index == 0: 
                index = index + 1
            if arr[index] >= arr[index - 1]: 
                index = index + 1
            else: 
                arr[index], arr[index-1] = arr[index-1], arr[index] 
                index = index - 1
  
        return arr

test_array = [2,7,1,9,5,8]
result = gnome_Sort(test_array)

print(result)

# Test Output: [1, 2, 5, 7, 8, 9]