# cook your dish here
T = int(input())

A = []
for i in range(0,T):
    N = int(input())
    S = [int(i) for i in input()]
    num_of_ones = S.count(1)
    ans = (num_of_ones*(num_of_ones+1))/2
    A.append(ans)
    
for i in A:
    print(int(i))