'''
Complexity of this sorting algorith is :
Worst-case performance - O(n^2)
Best-case performance - O(n)
Average performance - O(n^2)
The algorithm differs from a bubble sort
in that it sorts in both directions
on each pass through the list.
'''
def cocktailSort(list):
    left = 0
    right = len(list)
    for i in range(len(list)-1): # run through the list of elements
        ''' 
        with this if we decide if we should 
        iterate from left to right or right to left 
        '''
        if i % 2 == 0:
            max = list[left]
            thesi = left
            for j in range(left+1,right):
                if max < list[j]:
                    max = list[j]
                    thesi = j
                else:
                    list[thesi], list[j] = list[j], list[thesi]
            right -= 1
        elif i % 2 == 1:
            min = list[right]
            thesi = right
            for j in range(right-1,left):
                if min > list[j]:
                    min = list[j]
                    thesi = j
                else:
                    list[thesi], list[j] = list[j], list[thesi]
            left += 1
    return list

list = [8, 4, 2, 1, 10, 9, 12, 7]
sortedlist = cocktailSort(list)
print(sortedlist)
