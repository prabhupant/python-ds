"""
Awesome explanation - https://youtu.be/1LkOrc-Le-Y

Median is the middle element in a sorted array. The stream of input
integers can be in any order and we will have to store the integers in
such a way that the stream is maintained in an increasing order.

So the main idea is that take an array and divide it into two parts of 
equal length and the median will be as follows - 

* if the total number of integers in the stream is even, then both part will
have the same length. Hence the median will be the average of last element of the first 
part (i.e max element of the first part) and the first element of the second part (i.e 
min element of the second part)

* if total number of integers in the stream is odd, add the extra element in the first part.
In this case, the median will be the last element of the first part

Now we just have to maintain the order of both the parts of the array. Since we want the max
element from the first part, we can use a max heap there. And we can use min heap for the second
part as we need the min element from the second part

Time complexity:
    if the size of stream is N, we will have to iterate N times. LogN because insertion in heap
    takes this much time. O(1) for getting the max or min element

    N * LogN
"""

from heapq import heappush, heappop, heapify

class MedianStream:

    def __init__(self):
        self.stream = []
        self.min_heap = []
        self.max_heap = []
        heapify(self.max_heap)
        heapify(self.min_heap)
        self.curr_median = None
    
    
    def add_number(self, num):
        """
        min heap length <= maxheap length <= min heap length + 1
        """
        self.stream.append(num)

        if len(self.max_heap) == len(self.min_heap) == 0:
            self.curr_median = num

        if len(self.max_heap) > len(self.min_heap):
            if num < self.curr_median:
                max_popped = -1 * heappop(self.max_heap)
                heappush(self.min_heap, max_popped)
                heappush(self.max_heap, -1 * num)
                self.find_median('avg')
            else:
                heappush(self.min_heap, num)
                self.find_median('avg')
        else:
            if num > self.curr_median:
                # num will go to the min heap and the min element
                # of min heap will go the max heap
                min_popped = heappop(self.min_heap)
                heappush(self.max_heap, -1 * min_popped)
                heappush(self.min_heap, num)
                self.find_median('max')

            else:
                # num will go to the max heap
                heappush(self.max_heap, -1 * num)
                self.find_median('max')
    

    def find_median(self, how):
        if how == 'max':
            self.curr_median = -1 * self.max_heap[0]
        elif how == 'avg':
            self.curr_median = (self.min_heap[0] + (-1 * self.max_heap[0])) / 2
    

x = MedianStream()

num = input()

while num != 'q':
    if num == 's':
        print('Stream of integers - ', x.stream)
    else:
        num = int(num)
        x.add_number(num)
        print('Median - ', x.curr_median)
    
    num = input()
