
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index



def selectionSort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    
    return newArr

array = [100, 5, 72, 41, 80, 1, 99, 36, 27, 78]

print(selectionSort(array)) # [1, 5, 27, 36, 41, 72, 78, 80, 99, 100]