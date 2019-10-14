


#define your graph like a 2D matrix or use map function to take
#it as input from the user
l=[[1,0,1],
   [1,0,1],
   [0,1,0]]

d=[[False for i in range (len(l[0]))] for i in range(len(l))]



def dfs(i,j):
    
    if(d[i][j] ==False):
        d[i][j]=True
        if(i+1<len(l) and l[i+1][j]==1):
            dfs(i+1,j)
        if(i-1>=0 and l[i-1][j]==1):
            dfs(i-1,j)
        if(j+1<len(l[0]) and l[i][j+1]==1):
            dfs(i,j+1)
        if(j-1>=0 and l[i][j-1]==1):
            dfs(i,j-1)

no_forests=0

for i in range(len(l)):
    for j in range(len(l[0])):
        if d[i][j] == False and l[i][j]==1:
            no_forests+=1
            dfs(i,j)

print(no_forests)
        
