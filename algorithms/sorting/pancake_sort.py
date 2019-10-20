#pancake sorting
#used for the problem of sorting a disordered stack of pancakes in order by size
#Spatula can be placed anywhere in the stack to flip pancakes
#a pancake number is the minimum number of flips required for a given number of pancakes
#the goal is to sort in as few flips as possible

#reverse array [0..i]
def flip(arr, i):
    start = 0
    while start < i:
        tmp = arr[start]
        arr[start] = arr[i]
        arr[i] = tmp
        start += 1
        i -= 1

#get index of max elemt in array [0..n-1]
def getMax(arr, n):
    maxIndex = 0
    for i in range(0,n):
        if arr[i] > arr[maxIndex]:
            maxIndex = i
    return maxIndex

#main function that sorts
def pancakeSort(arr, n):
    size = n
    while size >1:
        maxIndex = getMax(arr, size)
        if maxIndex != size-1:
            flip(arr, maxIndex)
            flip(arr, size-1)
        size -= 1
