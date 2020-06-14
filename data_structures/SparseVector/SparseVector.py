from fractions import Fraction
class SparseVector():

    # List initialization:
    # we pass number of zeros in the list
    # so, at first we have n zeros in the list
    # list[0] = 0; list[1] = 0 ... list[n-1] = 0
    # Sparse vector's trong side is that we are saving memory
    # There is no 0s in the memory

    def __init__(self, n):
        self.data = list()
        self.zeros = n
    
    def push(self, i, val):
        incIdx = False
        insertIdx = -1

        newElem = (i, val)
        for idx in range(0, len(self.data)):
            elem = self.data[idx]
            if elem[0] >= i and incIdx == False:
                self.data[idx] = (elem[0] + 1, elem[1])
                incIdx = True
                insertIdx = idx
            if incIdx:
                self.data[idx] = (elem[0] + 1, elem[1])

        if incIdx:
            self.data.insert(insertIdx, newElem)
            return

        self.data.append(newElem)

    def get(self, i):
        for k in self.data:
            if k[0] == i:
                return k[1]

        return 0

    def count(self):
        return len(self.data) + self.zeros

    def printVector(self):
        vec = ""
        for i in range(0, self.count()):
            vec += str(self.get(i)) + " | "
        print(vec)
