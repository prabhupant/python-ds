# Linear Search
'''
Start with the Left Most element and end with the right most element.
Time Complexity => O(n)
'''

#1 Technique
def using_in_operator(x,arr):
    if(x in arr):
        print(arr.index(x))

using_in_operator(3,[1,2,3,4,5])

#2 Technique
def search(x,arr):
    for i in range(len(arr)):
        if(arr[i] == x):
            return i
    return -1

print("Found at : " + search(3,[1,2,3,4,5]))
print("Found at : " + search(0,[1,2,3,4,5]))