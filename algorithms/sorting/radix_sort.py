"""
Radix sort does sorting by going digit to digit from the least significant to the most
significant one. Its running time is dependant on the base and if it's a big base it can
run in O(n). Otherwise we get O((n+b) * logb(k)), see https://www.geeksforgeeks.org/radix-sort/
for an explanation.
"""

from math import log10
from random import randint

def get_digit(number, base, pos):
  return (number // base ** pos) % base

def prefix_sum(array):
  for i in range(1, len(array)):
    array[i] = array[i] + array[i-1]
  return array

def radixsort(l, base=10):
  passes = int(log10(max(l))+1)
  output = [0] * len(l)

  for pos in range(passes):
    count = [0] * base

    for i in l:
      digit = get_digit(i, base, pos)
      count[digit] +=1

    count = prefix_sum(count)

    for i in reversed(l):
      digit = get_digit(i, base, pos)
      count[digit] -= 1
      new_pos = count[digit]
      output[new_pos] = i

    l = list(output)
  return output

bef = [12,54,23,78,120,3423,342]
new = radixsort(bef)

print bef
print new
