from numpy import array, random, zeros
# @author  HBaena
# @profile https://github.com/HBaena/

# Exclusive for integers
# Dependeing of max and min values this algorithm will need a lot of memory
# But less processor
# 
def count_sort_list(unsort:array, reverse:str=False) -> list:
    min_val = min(unsort)
    max_val = max(unsort)

    histogram = [0]*(max_val - min_val + 1)

    for n in unsort:
        histogram[n - min_val] += 1 

    i = 0
    out = [0]*len(unsort)

    if not reverse:
        direction = range(max_val - min_val, -1   , -1)
    else:
        direction = range(0, max_val - min_val + 1,  1)
    
    for  j in direction:
        while histogram[j]: 
            out[i] = min_val + j
            i += 1
            histogram[j] -= 1
    return out

def count_sort_numpy(unsort:array, reverse:str=False) -> array:
    min_val = unsort.min()
    max_val = unsort.max()

    histogram = zeros(max_val - min_val + 1, dtype='int')

    for n in unsort:
        histogram[n - min_val] += 1 

    i = 0
    out = zeros(unsort.size, dtype='int')

    if not reverse:
        direction = range(max_val - min_val, -1   , -1)
    else:
        direction = range(0, max_val - min_val + 1,  1)
    
    for  j in direction:
        while histogram[j]: 
            out[i] = min_val + j
            i += 1
            histogram[j] -= 1
    return out


random_array = random.randint(-1000, 1000, 50, dtype='int')

print(list(count_sort_numpy(random_array, reverse=False)))
print(list(count_sort_numpy(random_array, reverse=True)))

print(list(count_sort_list(random_array, reverse=False)))
print(list(count_sort_list(random_array, reverse=True)))
