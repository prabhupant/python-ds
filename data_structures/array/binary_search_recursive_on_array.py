top=low
bottom=high
def binary_search_recursive(lst, item, top, bottom):
    mid=(top+bottom)//2
    if lst[mid]==item:
        return mid
    elif top>bottom:
        return -1
    elif lst[mid]<item:
        return binary_search_recursive(lst, item, mid+1, bottom)
    elif lst[mid]>item:
        return binary_search_recursive(lst, item, top, mid-1)
