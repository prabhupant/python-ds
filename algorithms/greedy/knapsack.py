"""
HIGHER DESCRIPTION

    The knapsack problem is one of the most common problems that are
    presented to people who are new to greedy algorithms. The concept is
    simple, you got a sack which has N space units and you got items that
    you want to put in the sack which have a Size and a Price. Your goal
    is to get the maximum value of items into the sack. A greedy algorithm
    approach to this problem is to select on each step the item with the
    smallest size, let's look at the code.
"""

class Item:
    price = 0
    size = 0

    def __init__(self, size, price):
        self.price = price
        self.size = size

items = []

# Feel free to change these values
# and add your own
items.append(Item(22,12))
items.append(Item(10,9))
items.append(Item(9,9))
items.append(Item(7,6))

# items is the items array
# N is the units of space our sack has 
def smallestSize(items,N):

    price = 0

    while(1):

        # Check if array is empty
        if(len(items) == 0):
            return price

        # Get the index of the smallest item
        currentItemIndex = findSmallestIndexOfItem(items)

        # Get the smallest item
        currentItem = items[currentItemIndex]

        # In case the next item that we have selected cannot
        # fit in the sack end the program, otherwise add it to
        # the sack and add it's price to the price variable
        if (N-currentItem.size >= 0):
            price+=currentItem.price
            N-=currentItem.size
            del items[currentItemIndex]
        else:
            return price

# Just a dummy code to find the smallest item
def findSmallestIndexOfItem(items):

    minimum = items[0].size
    index = 0
    counter = 0
    for item in items:
        if(item.size < minimum):
             minimum = item.size
             index = counter
             
        counter+=1

    return index
             

print(smallestSize(items,80))
