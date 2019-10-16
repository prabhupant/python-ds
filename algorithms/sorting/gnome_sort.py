'''
Gnome sort
Similar to insertion sort, every element is set into place 
one after another. 

Runtime complexity:
   Averages in O(n*n) 
'''

def swap( array, first, second ):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp
    return array

def gnomeSort(array):
    length = len(array)
    pos = 0 
    while (pos < length) :
        if pos == 0 or array[pos] >= array[pos - 1]:
            pos = pos + 1
        else:
            array = swap( array, pos, pos - 1)
            pos = pos - 1
    return array
    
