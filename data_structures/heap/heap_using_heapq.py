"""
Heap in python using heapq library function

Note: by default, heapq creates a min-heap. To make it a 
max-heap, add items after multiplying them by -1
"""

from heapq import heappop, heappush, heapify

heap = []
heapify(heap)

heappush(heap, 10)
heappush(heap, 11)
heappush(heap, 2)
heappush(heap, 4)
heappush(heap, 14)
heappush(heap, 1)

print('first element - ', heap[0])
print('popping min element - ', heappop(heap))
print('first element - ', heap[0])

# Heap prints as an array and can be access using indexes
print(heap)
print(heap[2])
