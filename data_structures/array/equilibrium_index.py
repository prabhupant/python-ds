# Find the equilibrium index of an array. An equilibrium index is such that
# the sum of elements to the left of it is equal to sum of elements to the right
# of it

def find_equi(arr):
    total_sum = sum(arr)

    left_sum = 0 

    for i, num in enumerate(arr):
        
        total_sum -= num
        
        if left_sum == total_sum:
            return i

        left_sum += num

    return -1


arr = [-7, 1, 5, 2, -4, 3, 0] 
print(find_equi(arr))
