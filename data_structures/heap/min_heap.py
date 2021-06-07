"""
See max_heap.py for more detailed comments
"""

class MinHeap:


    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.first = 0
        self.heap = [0] * self.maxsize


    def is_empty(self):
        return self.size == 0


    def is_leaf(self, pos):
        if self.mid_index() <= pos <= self.last_index():
            return True
        return False


    def parent(self, pos):
        return pos // 2


    def left_child(self, pos):
        return 2*pos + 1


    def right_child(self, pos):
        return 2*pos + 2


    def last_index(self):
        return self.size - 1


    def mid_index(self):
        return self.size // 2


    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]


    def pop_min(self):
        min_element = self.heap[self.first]
        self.heap[self.first] = self.heap[self.last_index()]
        self.heap[self.last_index()] = 0
        self.size -= 1
        self.min_heapify(self.first)
        return min_element


    def min_heapify(self, pos):
        if not self.is_leaf(pos):
            left = self.heap[self.left_child(pos)]
            right = self.heap[self.right_child(pos)]
            curr = self.heap[pos]

            if curr > left or curr > right:

                if left > right:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))
    

    def insert(self, element):
        if self.is_empty():
            self.heap[self.first] = element
            self.size += 1
            return

        if self.size >= self.maxsize:
            return

        self.size += 1
        self.heap[self.last_index()] = element

        curr = self.last_index()

        while self.heap[curr] < self.heap[self.parent(curr)]:
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)


    def print(self):
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
    min_heap = MinHeap(15)
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(17)
    min_heap.insert(10)
    min_heap.insert(84)
    min_heap.insert(19)
    min_heap.insert(6)
    min_heap.insert(22)
    min_heap.insert(9)

    min_heap.print()
    print(min_heap.heap)
    print('Min element is - ', min_heap.pop_min())
    min_heap.print()
