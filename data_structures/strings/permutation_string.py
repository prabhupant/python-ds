def permutations(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return s
    # Find the permutations for s if there are
    # more than 1 characters
    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(s)):
       m = s[i]
       # Extract s[i] or m from the list.  remLst is
       # remaining list
       rems = s[:i] + s[i+1:]
       # Generating all permutations where m is first
       # element
       for p in permutations(rems):
           l.append(m + p)
    return l
for i in permutations('123'):
    print(i,end=',')
