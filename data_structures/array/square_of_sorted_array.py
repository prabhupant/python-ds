def square(arr):
    n = len(arr)
    j = 0
    
    # Counting the number of negative elements 
    while j < n and arr[j] < 0:
        j += 1
    
    i = j - 1 # index of last negative element
    ans = []

    while 0 <= i and j < n:
        if arr[i] ** 2 < arr[j] ** 2:
            ans.append(arr[i] ** 2)
            i -= 1
        else:
            ans.append(arr[j] ** 2)
            j += 1

    while i >= 0:
        ans.append(arr[i] ** 2)
        i -= 1
    
    while j < n:
        ans.append(arr[j] ** 2)
        j += 1

    return ans





