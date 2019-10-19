# given a matrix find the length of rivers denoted by one on horizontal and vertical connections
# the 0s represent part of land
# eg |0 0 0 0 0 0| in this output should be [3,1]
#   |1 1 1 0 0 1|
# assuming rivers never diverge


# main function
def riverSize(matrix):
    size = []
    visited = [[False for value in row] for row in matrix]
    print(visited)
    for i in range(len(matrix)):
        for j in range(len(matrix(i))):
            if j in visited:
                continue
            traverseNode(i,j,matrix,visited,sizes)
    return size

def traverseNode(i,j,matrix,visited,sizes):
    count=0
    #stack because u=we are using defs
    nodestoexplore = [[i,j]]
    #a node can be appended to this that will be explored by the time it reaches it
    while len(nodestoexplore):
        currentnode = nodestoexplore.pop()
        i = currentnode[0]
        j = currentnode[1]
        if visited[i][j]:
            continue
        visited[i][j]=True
        if matrix[i][j]==0:
            continue
        count+=1
        unvisitedneighbours = getUnvisitedNeighbours(i,j,matrix,visited)
        for neighbour in unvisitedneighbours:
            nodestoexplore.append(unvisitedneighbours)
        if count>0:
            sizes.append(count)
def getUnvisitedNeightbours(i,j,matrix,visited):
    unv = []
    if i>0 and not visited[i-1][j]:
        unv.append([i-1,j])
    if i<len(matrix)-1 and not visited[i+1][j]:
        unv.append([i+1,j])
    if j>0 and not visited[i][j-1]:
        unv.append([i,j-1])
    if j<len(matrix[0])-1 and not visited[i][j+1]:
        unv.append([i,j+1])
    return unv
