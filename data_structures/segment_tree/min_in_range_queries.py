'''
Question:
Given an array A of size N, there are two types of queries on this array.
1. q l r: In this query you need to print the minimum in the sub-array .
2. u l r v In this query you need to update the range from l to r by v.

Time Complexity:
update query: log(n)
min in range query: log(n)
'''

import math as mt

class SegmentTree:
    def __init__(self, array):
        self.MAX_INT = 2**31-1
        self.src = array
        self.len = len(array)
        self.total_nodes = (2**mt.ceil(mt.log(self.len, 2))*2-1)
        self.tree = [0] * self.total_nodes
        self.dues = [0] * self.total_nodes

    def build(self):
        self.build_tree(l=0, r=self.len-1, par=0)
        
    def build_tree(self, l, r, par):
        if l == r:
            self.tree[par] = self.src[l]
            return
        div = (l+r)//2
        self.build_tree(l, div, (par<<1)+1)
        self.build_tree(div+1, r, (par<<1)+2)
        self.tree[par]=min(self.tree[(par<<1)+1], self.tree[(par<<1)+2])

    def min_in_range(self, low, high):
        return self.min_(low, high, 0, self.len-1, 0)

    def min_(self, low, high, left, right, par):
        if low > right or high < left:
            return self.MAX_INT
        
        if self.dues[par] > 0:
            self.tree[par] += self.dues[par]
            if left is not right:
                self.dues[(par<<1)+1] += self.dues[par]
                self.dues[(par<<1)+2] += self.dues[par]
            self.dues[par]=0;
            
        if low <= left and high >= right:
            return self.tree[par]
        
        div = int((right+left)/2)
        
        return min(self.min_(low, high, left, div, (par<<1)+1),
                   self.min_(low, high, div+1, right, (par<<1)+2) )

    def update_range(self, low, high, value):
        return self.update(low, high, value, 0, self.len-1, 0)

    def update(self, low, high, value, left, right, par):
        if self.dues[par] > 0:
            self.tree[par] += self.dues[par]
            if left is not right:
                self.dues[(par<<1)+1] += self.dues[par]
                self.dues[(par<<1)+2] += self.dues[par]
            self.dues[par]=0;

        if low > right or high < left:
            return;

        if low <= left and high >= right:
            self.tree[par] += value
            if(left is not right):
                self.dues[(par<<1)+1] += value
                self.dues[(par<<1)+2] += value
            return

        div = (right+left)//2
        self.update(low, high, value, left, div, (par<<1)+1)
        self.update(low, high, value, div+1, right, (par<<1)+2)
        

if __name__=='__main__':
    
    array = list(map(int, input('Enter space seprated number\n').strip().split(' ')))
    sg = SegmentTree(array)
    sg.build()
    
    n_query = int(input('Enter number of queries\n'))
    print('Query format\nq low high (to find minimum in range e.g: q 0 3)\nu low high value (to add "value" to all elements e.g: u 3 4 99)')
    
    while n_query:
        n_query -= 1
        args = input('Enter query: ').strip().split(' ')
        if args[0] == 'q' and len(args) == 3:
            print(sg.min_in_range(low=int(args[1]), high=int(args[2])))
        elif args[0] == 'u' and len(args) == 4:
            sg.update_range(low=int(args[1]), high=int(args[2]), value=int(args[3]))
            print('Update Successfully!')
        else:
            print('Invalid query format')
            n_query += 1
                
        


        
