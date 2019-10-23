# Binary Search
'''
This Works on a Sorted Array.
Time Complexity => O(log n)
'''
# Solved Using Recursion.
def binary(a, first, last, term):
    mid=int((first+last)/2)
    if term>a[mid]:
        binary(a, mid, last, term)
    elif term<a[mid]:
        binary(a,first, mid, term)
    elif term==a[mid]:
        print("Number found at", mid+1)
    else:
        print("Number is not there in the array")

arr = [1,2,3,4,5]

to_be_found = 4

binary(arr,0,len(arr),to_be_found)