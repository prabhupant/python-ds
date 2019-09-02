# Use these facts - 

# If there are even number of negative numbers and no zeros,
# then the min product is the product of all except the max
# negative value

# If there are odd number of negative numbers and no zeros,
# the result is simply the product of all

# If there is a zero, then the result is zero

# If there are only positive numbers, the the result is
# the smallest positive number

def find(arr):
    if len(arr) == 1:
        return arr[0]
    
    count_negative = 0
    count_positive = 0
    count_zero = 0
    max_neg = float('-inf')
    min_pos = float('inf')
    
    prod = 1
    
    for num in arr:
        if num == 0:
            count_zero += 1
            continue

        if num < 0:
            count_neg += 1
            max_neg = max(max_neg, num)

        if num > 0:
            min_pos = min(min_pos, num)

        prod = prod * num

    if count_zero == len(arr) or (count_neg == 0 and count_zero > 0):
        return 0
    
    if count_neg == 0:
        return min_pos

    if count_neg & 1 == 0 and count_neg != 0:
        prod = int(prod / max_neg)
    
    return prod

