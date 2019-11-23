'''
Problem statement:
given an array of N elements,
return the length of the
longest increasing subsequence
of that array
'''

def memoize(f):
    """
    Generic decorator for
    Dynamic Programming
    problems
    """
    cache = dict()
    def memoized_f(*args):
        if args in cache:
            global hits
            hits += 1
            return cache[args]

        cache[args] = f(*args)
        return cache[args]

    return memoized_f


def lis(s):
    """ Return length of LIS in array s """

    '''
    NOTE: array s will be declared in the superscope
    of lis_routine, so it doesn't need to be passed
    as argument and subsequently not hashed by @memoize
    '''

    @memoize
    def lis_routine(cur_index=0, last_index=-1, cur_length=0):
        """
        Return length of the longest increasing
        subsequence from array s.

        To use, simply call lis(s). The other
        parameters will be used in the
        recursion
        """

        if cur_index == len(s):
            return cur_length   

        '''
        Length of the LIS if we include cur_index
        is initialized as -1 because we might not
        be able to include it if it is less than
        the number at last_index. If last_index is
        -1, we can take cur_index, as it will be
        the first integer in the possible LIS.
        '''
        take = -1
        if last_index == -1 or s[last_index] < s[cur_index]:
            take = lis_routine(cur_index + 1, cur_index, cur_length + 1)
        
        # Length of the LIS if we don't include cur_index
        not_take = lis_routine(cur_index + 1, last_index, cur_length)

        # Return the greatest LIS (include cur_index or not)
        return max(take, not_take)

    return lis_routine()


def main():
    """ Simple test cases """
    t1 = [1, 6, 2, 3, 7, 9, 4, 8, 5]
    t2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    t3 = [-1, -1, -1, -1, -1, -1]

    print('LIS of {}: {}'.format(t1, lis(t1)))   # Should be 5
    print('LIS of {}: {}'.format(t2, lis(t2)))   # Should be 1
    print('LIS of {}: {}'.format(t3, lis(t3)))   # Should be 1


if __name__ == '__main__':
    main()