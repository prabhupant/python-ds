#largest range
#find the greatest range of consecutive no in array in unsorted order

def maxRange(arr):
    best =[]
    longestlen = 0
    check = {}
    for i in arr:
        check[i]= True
    for i in arr:
        if not check[i]:
            continue
        check[i]=False
        curlen = 1
        left = i-1
        right = i+1
        while left in check:
            check[left] = False
            curlen+=1
            left-=1
        while right in check:
            check[right] = False
            curlen+=1
            right+=1
        if curlen > longestlen:
            longestlen =curlen
            best = [left+1,right-1]
    return best

print(maxRange([1,4,7,6,8,2,3]))
