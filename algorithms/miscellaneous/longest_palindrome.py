'''
finds the longest palindrome in a given string, the pallindrome
need not to be continous

input:
agbdba

output:
5
abdba
'''
s=input()
slength=len(s)

if(slength==1):
    print(1)
    
if(slength==2):
    if(s[0]==s[1]):
        print(2)
    else:
        print(1)
        

matrix=[[0 for i in range(slength)] for j in range(slength)]

for i in range(slength):
    matrix[i][i]=1

for l in range(2,slength+1):
    for i in range(slength-l+1):
        j=i+l-1
        if(s[i]==s[j]):
            matrix[i][j]=2+matrix[i+1][j-1]
        else:
            matrix[i][j]=max(matrix[i+1][j],matrix[i][j-1])

longestpall=matrix[0][slength-1]
print(longestpall)
'''
for i in matrix:
    print(i)
'''

