'''
Huffman Coding | Greedy algorithm
'''

import heapq

class Node:
    def __init__(self, frequency, symbol=None, left=None, right=None):
        self.f = frequency
        self.s = symbol
        self.l = left
        self.r = right
        
    def __lt__(self, other):
        return self.f < other.f

    def __str__(self):
        return "< "+str(self.s) +" "+ str(self.f)+" >"
    
class Huffman:
    
    def __init__(self, sym, freq):
        self.leaf = [Node(f, s) for s, f in zip(sym, freq)]
        self.codes = {}

    '''To build the huffman tree'''
    def build(self):
        heapq.heapify(self.leaf)
        
        while len(self.leaf) >= 2:
            l = heapq.heappop(self.leaf)
            r = heapq.heappop(self.leaf)
            root = Node(frequency=l.f+r.f, left=l, right=r)
            heapq.heappush(self.leaf, root)
            
        self.root = heapq.heappop(self.leaf)

    '''To find the encoded value for each symbols'''
    def encode(self):
        self.encoder(self.root, [None]*1000, 0)
        return self.codes

    def encoder(self, root, code, top):
        if root.l is not None:
            code[top]=0
            self.encoder(root.l, code, top+1)
        if root.r is not None:
            code[top]=1
            self.encoder(root.r, code, top+1)
        if root.s is not None:
            self.codes[root.s] = ''.join(map(str, code[:top]))
    

if __name__=='__main__':
    print('***** Example 1 *****\n')
    
    s = ['a', 'b', 'c', 'd', 'e', 'f']
    f = [5, 9, 12, 13, 16, 45]
    hm = Huffman(s, f)
    hm.build()
    codes = hm.encode()
    for s in codes:
        print(s, codes[s])

    print('\n***** Example 2 *****\n')
    
    text = 'This is an simple Hello world example'
    s_f = {}
    for c in text:
        if c not in s_f:
            s_f[c] = 1
        else:
            s_f[c] += 1
            
    hm2 = Huffman(s_f.keys(), s_f.values())
    hm2.build()
    hm2_codes = hm2.encode()
    print('Original text: ', text, '\nEncoded bits:', end=' ')
    for c in text:
        print(hm2_codes[c], end='')

