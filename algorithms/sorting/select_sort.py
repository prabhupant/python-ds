
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index



def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    
    return new_arr

array = [100, 5, 72, 41, 80, 1, 99, 36, 27, 78]

print(selection_sort(array)) # [1, 5, 27, 36, 41, 72, 78, 80, 99, 100]
