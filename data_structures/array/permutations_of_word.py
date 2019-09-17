def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        rem_lst = lst[:i] + lst[i+i:]
        for p in permutation(rem_lst):
            l.append([m] + p)
    return l


data = list('hello world')
for p in permutation(data):
    print(p)
