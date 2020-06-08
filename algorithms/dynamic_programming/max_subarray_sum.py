
MIN_VALUE = -100000000000000000000

def max_subarray_sum(a):
    max_so_far = MIN_VALUE
    max_ending_here = 0; 
  
    for i in range(0 , len(a)):
        max_ending_here = max_ending_here + a[i]; 
        if max_so_far < max_ending_here : 
            max_so_far = max_ending_here 
        if max_ending_here < 0: 
            max_ending_here = 0 
    
    return max_so_far
