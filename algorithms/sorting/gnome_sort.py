'''
Gnome sort is not best sorting algorithms but sure it takes its pride.
It has time O(n^2)
'''


def gnome_sort(arr):
    """
    Examples:
        >>> gnome_sort([0, 5, 2, 3, 2])
        [0, 2, 2, 3, 5]

        >>> gnome_sort([])
        []
        >>> gnome_sort([-2, -45, -5])
        [-45, -5, -2]
    """

    # first case
    size = len(arr)

    if size <= 1:
        return arr
    ind = 0
    # while loop
    while ind < size:
        if ind == 0:
            ind += 1
        elif arr[ind] >= arr[ind - 1]:
            ind += 1
        else:
            # swap
            temp = arr[ind - 1]
            arr[ind - 1] = arr[ind]
            arr[ind] = temp
            ind -= 1

    return arr
