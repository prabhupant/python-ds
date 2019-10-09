# cook your dish here
'''
Given a string S consisting of only 1s and 0s, find the number of substrings which start and end both in 1.
In this problem, a substring is defined as a sequence of continuous characters Si, Si+1, ..., Sj where 1 ≤ i ≤ j ≤ N.
Input:
First line contains T, the number of testcases. Each testcase consists of N(the length of string) in one line and string in second line.

Example
Input:
2
4
1111
5
10001

Output:
10
3
'''
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
