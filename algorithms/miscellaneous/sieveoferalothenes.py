import math
n=int(input("Enter the number"))
isPrime=[]
for i in range(n):
    isPrime.append(True)
isPrime[0]=False
isPrime[1]=False
for i in range(2,int(math.sqrt(n)),1):
    for j in range(2*i,n,i):
        isPrime[j]=False
for i in range(0,n,1):
    print(i,":",isPrime[i])