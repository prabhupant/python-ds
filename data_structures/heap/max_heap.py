"""
Thing to remember - 
* index of parent = i / 2
* index of left child = 2i + 1
* index of right child = 2i + 2
"""

class MaxHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0  # current number of elements in the heap
        self.heap = [0] * self.maxsize
        self.front = 0


    def parent(self, pos):
        return (pos) // 2


    def left_child(self, pos):
        return 2*pos + 1

    
    def right_child(self, pos):
        return 2*pos + 2


    def mid_index(self):
        return self.size // 2


    def last_index(self):
        return self.size - 1


    def is_leaf(self, pos):
        """
        Every node that is after the middle index of the heap
        is a leaf node because their children cannot exist as the
        index of children are twice their index as those indexes
        do not exist in the heap
        """
        if self.mid_index() <= pos <= self.last_index():
            return True
        return False


    def is_empty(self):
        if self.size == 0:
            return True
        return False

    
    def insert(self, value):
        if self.is_empty():  # if the heap is empty
            self.heap[self.front] = value
            self.size += 1
            return

        if self.size >= self.maxsize:  # if max size has been reached
            return

        self.size += 1
        self.heap[self.last_index()] = value

        curr = self.last_index()
        
        # While inserting the element in the heap we have to 
        # make sure that the inserted element is always smaller
        # than its parent. So basically here we are adjusting the 
        # position of the parent
        while self.heap[curr] > self.heap[self.parent(curr)]:
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)
    

    def max_heapify(self, pos):
        """
        This function will run whenever a node is non-leaf
        node and smaller than its childen
        """
        if not self.is_leaf(pos):
            left = self.heap[self.left_child(pos)]
            right = self.heap[self.right_child(pos)]
            curr = self.heap[pos]

            if curr < left or curr < right:
                
                # This check is only to prevent out-of-index error
                if left > right:
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))


    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    
    def pop_max(self):
        max_element = self.heap[self.front]  # max element is always at the front
        self.heap[self.front] = self.heap[self.last_index()]  # placing last element at the front
        self.heap[self.last_index()] = 0
        self.size -= 1  # decrease size as one element has been popped
        self.max_heapify(self.front)  # heapify the heap again
        return max_element


    def print(self):
        """
        Priting in inorder
        """
        for i in range(0, self.mid_index() + 1):
            parent = self.heap[i]
            left = self.heap[self.left_child(i)]
            right = self.heap[self.right_child(i)]

            print(f"Parent: {self.heap[i]}")

            if left:
                print(f"Left child: {left}")
            if right:
                print(f"Right child: {right}")


if __name__ == '__main__':
    max_heap = MaxHeap(15)
    max_heap.insert(5)
    max_heap.insert(3)
    max_heap.insert(17)
    max_heap.insert(10)
    max_heap.insert(84)
    max_heap.insert(19)
    max_heap.insert(6)
    max_heap.insert(22)
    max_heap.insert(9)

    max_heap.print()
    print('Max element is - ', max_heap.pop_max())
    max_heap.print()
