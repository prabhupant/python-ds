import sys

class MaxSegTree():

    def __init__(self, n, arr = None):
        self._t = [-sys.maxsize - 1] * (4 * n)
        self._n = n
        if arr: self._build(arr, 1 , 0 , n - 1)

    def _build(self, a, v, tl, tr):
        if tl == tr:
            self._t[v] = a[tl]
        else:
            tm = (tl + tr) // 2
            self._build(a, v*2, tl, tm)
            self._build(a, v*2+1, tm+1, tr)
            self._t[v] = max(self._t[v*2] ,self._t[v*2+1])

    def _max_util(self, v, tl, tr, l, r):
        if l > r: return -sys.maxsize - 1

        if l == tl and r == tr : return self._t[v]
        
        tm = (tl + tr) // 2
        return max(self._max_util(v*2, tl, tm, l, min(r, tm)) ,self._max_util(v*2+1, tm+1, tr, max(l, tm+1), r))
    
    def _update_util(self, v, tl, tr, pos, new_val):
        if tl == tr: 
            self._t[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm: self._update_util(v*2, tl, tm, pos, new_val)
            else: self._update_util(v*2+1, tm+1, tr, pos, new_val)
            self._t[v] = max(self._t[v*2] , self._t[v*2+1])

    def max_element(self, l, r):
        return self._max_util(1 , 0 , self._n - 1 , l , r)
    
    def update(self, pos, new_val):
        self._update_util(1 , 0 , self._n - 1 , pos , new_val)
    
    def add(self, pos, change):
        value = self.max_element(pos , pos)
        self._update_util(1 , 0 , self._n - 1 , pos , value + change)