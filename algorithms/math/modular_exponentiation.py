# to compute modular power 
  
# Iterative Function to calculate 
# (x^y)%p in O(log y)  


def power(x, y, p):
    res = 1     # Initialize result 
  
    # Update x if it is more than or equal to p
    x = x % p  
  
    while y > 0:
          
        # If y is odd, multiply x with result
        if y & 1 == 1:
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res


# TESTING
if __name__ == "__main__":
    assert power(2, 3, 5) == 3
    assert power(7, 3, 31) == 2
    print("Tests pass.")
