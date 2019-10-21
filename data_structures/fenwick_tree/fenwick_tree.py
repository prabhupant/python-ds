

# Returns the right most significant bit of an integer.
# For example, 12 is represented by 1100 in binary, so it's LSB is the third position, 4.
def LSB(n):
    return n & -n


class FenwickTree:
    '''
    A Fenwick Tree allows you to sum a range of elements and update an element in an array in O(log(n)). A segment tree
    can also achieve this, but it takes twice the memory, making it less memory efficient. On the other hand, a segment tree
    can compute more functions in a range of elements, like the minimum or maximum.
    The way it works is that given an index (note that we start with 1 and not 0), the element in the array will be the sum 
    of the LSB(index) elements below (including index). For example: with index 3, 3 = 11 in binary, and LSB(3) = 1, so this
    element is equal to the corresponding element in the original array. But 4 = 100 in binary, so LSB(4) = 4, so it is equal
    to the sum of A[0] + A[1] + A[2] + A[3] (the first 4 elements of the original array).
    '''

    def __init__(self, array):
        self.len = len(array)+1
        # Initialize an array of length n+1 to 0
        self.arr = [0] * self.len
        # Update the array to the one passed in the parameters
        for i in range(0, self.len - 1):
            self.update(i, array[i])

    def update(self, index, val):
        j = index+1
        # Update the value for every element that sums A[index]
        while j < self.len:
            self.arr[j] += val
            j += LSB(j)

    # Get the sum of all elements before index (included)
    def get_sum(self, index):
        sum = 0
        index += 1
        while index > 0:
            sum += self.arr[index]
            index -= LSB(index)
        return sum

    # Get the sum of all elements in the range [start, end]
    def get_sum_range(self, start, end):
        return self.get_sum(end) - self.get_sum(start-1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    fw = FenwickTree(arr)
    print(fw.get_sum(3))
    print(fw.get_sum(5))
    print(fw.get_sum_range(1, 7))
