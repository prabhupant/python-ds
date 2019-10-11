from random import randint
# @author  HBaena
# @profile https://github.com/HBaena/

# Exclusive for integers
# Dependeing of max and min values this algorithm will need a lot of memory
# But less processor

'''
This algorithm only works with an integer array.
basically, it creates a histogram with all possible numbers between the min and max 
values of the array. Thus, if the histogram has a value not zero in any position, 
it indicates if the number corresponding to the position is in the array and how many 
times it is repeated too.
'''
def count_sort(unsort:list, reverse:str=False) -> list:
    # Calculate min and max values
    min_val = min(unsort)
    max_val = max(unsort)
    # create and empty array of all values between min and max values and it is started with zeros  
    histogram = [0]*(max_val - min_val + 1)
    
    for n in unsort:
        # Histogram is increased by one for each value in the unsorted array
        # if n = min_values the position 0 is increased
        # if n = min_values the position 1 and so on
        histogram[n - min_val] += 1 

    i = 0
    # The out array must be of the same lenght of unsorted array
    out = [0]*len(unsort)
    if not reverse:
        direction = range(max_val - min_val, -1   , -1)
    else:
        direction = range(0, max_val - min_val + 1,  1)
    
    for  j in direction:
        # if histogram is not zero, the values min_val + j is added to the out array
        while histogram[j]: 
            out[i] = min_val + j
            i += 1
            histogram[j] -= 1
    return out

random_array = [randint(-1000, 1000) for _ in range(100)]

print(list(count_sort(random_array, reverse=False)))
print(list(count_sort(random_array, reverse=True)))
