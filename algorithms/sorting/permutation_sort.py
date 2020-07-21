import random

# Sorts array a[0..n-1] using Bogo sort


def bogo_sort(a):
    n = len(a)
    while not is_sorted(a):
        shuffle(a)

# To check if array is sorted or not


def is_sorted(a):
    n = len(a)
    for _ in range(0, n - 1):
        if a[i] > a[i + 1]:
            return False
    return True

# To generate permutation of the array


def shuffle(a):
    n = len(a)
    for _ in range(0, n):
        r = random.randint(0, n - 1)
        a[i], a[r] = a[r], a[i]


# Driver code to test above
b = [3, 2, 4, 1, 0, 5]
bogo_sort(b)
print("Sorted array :")
for i in range(len(b)):
    print("%d" % b[i]),
