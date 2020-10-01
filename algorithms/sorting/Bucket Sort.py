def IS(a):
    n=len(a)
    for i in range(1,n):
        m=i
        temp=a[m]
        while(m>0 and temp<a[m-1]):
            a[m]=a[m-1]
            m=m-1
        a[m]=temp   

def bucket_sort(arr):
    n=len(arr)
    maxval=max(arr)
    size=maxval/n
    bucket=[list() for x in range(n)]
    for x in range(n):
        i=int(arr[x]/size)
        if i!=n:
            bucket[i].append(arr[x])
        else:
            bucket[n-1].append(arr[x])
    for x in bucket:
        IS(x)
    ans=[]
    for x in range(n):
        ans+=bucket[x]
    return ans    
    
arr=[2.4,2.6,2,5.6,3.6,1.7]
b=bucket_sort(arr)
print(*b)
