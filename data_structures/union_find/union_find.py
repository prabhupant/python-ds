
class UnionFind():

    def __init__(self, n, arr):

        self.size = n
        self.store = arr
        self.parent = [-1]*self.size
    '''
        To find the parent of the value
    '''
    def find_parent(self, val):

        if self.parent[val] == -1:
            return val
        else:
            return self.find_parent(self.parent[val])
    '''
        Make a union for two values
    '''
    def union(self, x, y):

        x_par = self.find_parent(x)
        y_par = self.find_parent(y)
        self.parent[x_par] = y_par

n = 5
store = [13, 34, 21, 32, 22]
uf = UnionFind(n, store)
uf.union(1, 4)
print (uf.find_parent(1))
print (uf.find_parent(4))
