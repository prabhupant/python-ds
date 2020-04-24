def front_and_back_search(lst, item):
    '''
    args:
    lst: an unsorted array of integers
    item: data to be found

    return:
    item which is found else False
    '''
    rear=0
    front=len(lst)-1
    u=None
    if rear>front:
        return False
    else:
        while rear<=front:
            if item==lst[rear] or item==lst[front]:
                u=''
                return True ##item found
            elif item!=lst[rear] and item!=lst[front]:
                if item > lst[rear]:
                    rear=rear+1
                elif item < lst[front]:
                    front=front-1
        if u==None:
            return False
