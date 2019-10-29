'''
Bubble Sort worst time complexity occurs when array is reverse sorted - O(n^2)
Best time scenario is when array is already sorted - O(n)
'''

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]