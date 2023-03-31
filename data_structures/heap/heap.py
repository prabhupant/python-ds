class MaxHeap():
    def __init__(self):
        self.arr = [None]
    

    def insert(self, val):
        self.arr.append(val)

        if len(self.arr) == 2:
            return 

        parentIdx = (len(self.arr)-1)//2

        while(parentIdx > 0):
            if(self.arr[parentIdx] < val):
                childIdx = self.arr.index(val)
                temp = self.arr[parentIdx]
                self.arr[parentIdx] = self.arr[childIdx]
                self.arr[childIdx] = temp


            parentIdx = parentIdx//2
        return 

    def deleteMax(self):
        lastIdx = len(self.arr) - 1
        rootIdx = 1

        temp = self.arr[lastIdx]
        root = self.arr[rootIdx]
        self.arr[lastIdx] = root
        self.arr[rootIdx] = temp

        self.arr.pop(-1)

        idx = 1
        while((2*idx + 1) < len(self.arr)):
            replace = max(self.arr[2*idx], self.arr[2*idx + 1])
            replaceIdx = self.arr.index(replace)
            original = self.arr[idx]

            if(self.arr[idx] < self.arr[replaceIdx]):
                self.arr[idx] = replace
                self.arr[replaceIdx] = original 
                idx = self.arr.index(original)
            else:
                break

        return self.arr



heap = MaxHeap()
arr = [9,8,6,5,2,1]

for i in range(0, len(arr)):
    heap.insert(arr[i])
    print("INSERT:::::" + str(heap.arr))
heap.insert(7)
heap.insert(10)
print("INSERT:::::" + str(heap.arr))

heap.deleteMax()
print("DELETE:::::" + str(heap.arr))