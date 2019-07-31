def partition(arr):
    s = sum(arr)
    if not s % 3 == 0:
        return False
    s = s / 3
    targets = [2*s, s]
    acc = 0

    for a in arr:
        acc += a
        if acc == targets[-1]:
            targets.pop()
        if not targets:
            return True
    
    return False
