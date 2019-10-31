def find_odd_number(nums):
    """ Find one number in array which is not duplicated,
        or exsits odd times.
    """
    s = 0 
    for n in nums:
        s ^= n 
    return s 


a = [0, 0, 1, 1, 2, 2, 6, 6, 9, 10, 10] 
print(find_odd_number(a))
