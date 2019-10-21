

# Returns the right most significant bit of an integer.
# For example, 12 is represented by 1100 in binary, so it's LSB is the third position, 4.
def LSB(n):
    return n & -n


class FenwickTree:
    def __init__(self, array):
        self.len = len(array)+1
        self.arr = [0] * self.len
        for i in range(0, self.len - 1):
            self.update(i, array[i])

    def update(self, index, val):
        j = index+1
        while j < self.len:
            self.arr[j] += val
            j += LSB(j)

    def get_sum(self, index):
        sum = 0
        index += 1
        while index > 0:
            sum += self.arr[index]
            index -= LSB(index)
        return sum

    def get_sum_range(self, start, end):
        return self.get_sum(end) - self.get_sum(start-1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    fw = FenwickTree(arr)
    print(fw.get_sum(3))
    print(fw.get_sum(5))
    print(fw.get_sum_range(1, 7))
