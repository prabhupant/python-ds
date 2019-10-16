'''
Gnome sort
Similar to insertion sort, every element is set into place 
one after another. Check each element pair whether they are in place 
or not. "Bubble" element to the left if not in place.

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
    

test_array = [-19,30,11,100,-30,5,1,200,34]

test_array = gnomeSort(test_array)

print(test_array)