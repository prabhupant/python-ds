def front_and_back_search(lst, item):
    """
    args:
    lst: an unsorted array of integers
    item: data to be found

    return:
    item which is found else False
    """
    rear = 0
    front = len(lst) - 1
    u = None
    if rear > front:
        return False
    else:
        while rear <= front:
            if item == lst[rear] or item == lst[front]:
                u = ''
                return True  # item found
            else:
                rear = rear + 1
                front = front - 1
        if u is None:
            return False


# TESTING
if __name__ == "__main__":
    import random
    SIZE = 10000

    UNSORTED = [i for i in range(SIZE)]
    random.shuffle(UNSORTED)

    for i in range(SIZE):
        assert front_and_back_search(UNSORTED, i)

    assert not front_and_back_search(UNSORTED, SIZE + 1)

    print("Tests pass.")
