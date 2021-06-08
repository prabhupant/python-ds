"""
Use a priority queue - min heap

as soon as the stream reaches a length of K, start finding the number

Since we are using a priority queue (min heap), the minimum number will be 
at the first index. O(1) time to extract it

We have to make sure that the length of the stream does not go above K because
we to find the kth largest element which in terms of this heap means the smallest
element. For example lets say we have K = 4. So as soon as the stream reaches a 
length of 4, we start to find the 4th largest number. Now as we are maintaining the 
length of the array at 4, 4th largest number will mean the smallest number. Using this
we are designing the program.

If the number entered in the stream is less than the current min, we dont take it as it
wont affect the result.
"""

from heapq import heapify, heappop, heappush

class Stream:

    def __init__(self, k):
        self.heap = []
        self.stream = []
        self.k = k
        self.curr_min = None
        heapify(self.heap)


    def insert(self, x):
        self.stream.append(x)

        if len(self.heap) < self.k: # when the heap is empty or size is less than K
            heappush(self.heap, x)
            self.curr_min = self.heap[0]
        else:
            if x > self.curr_min:
                heappop(self.heap)  # remove the curr min element
                heappush(self.heap, x)  # insert x
                self.curr_min = self.heap[0]
                

    def find_kth_max(self):
        if len(self.heap) == self.k:
            print(f'{self.k}th max number - {self.heap[0]}')

k = 3
x = Stream(k)

num = input()

while num != 'q':
    if num == 's':
        print(f'Stream - {x.stream} | K - {k}')
    else:
        num = int(num)
        x.insert(num)
        x.find_kth_max()
    num = input()
