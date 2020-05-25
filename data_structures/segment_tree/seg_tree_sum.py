class SumSegTree():

    def __init__(self, n, arr = None):
        self._t = [0] * (4 * n)
        self._n = n
        if arr: self._build(arr, 1 , 0 , n - 1)

    def _build(self, a, v, tl, tr):
        if tl == tr:
            self._t[v] = a[tl]
        else:
            tm = (tl + tr) // 2
            self._build(a, v*2, tl, tm)
            self._build(a, v*2+1, tm+1, tr)
            self._t[v] = self._t[v*2] + self._t[v*2+1]

    def _sum_util(self, v, tl, tr, l, r):
        if l > r: return 0

        if l == tl and r == tr : return self._t[v]
        
        tm = (tl + tr) // 2
        return self._sum_util(v*2, tl, tm, l, min(r, tm)) + self._sum_util(v*2+1, tm+1, tr, max(l, tm+1), r)
    
    def _update_util(self, v, tl, tr, pos, new_val):
        if tl == tr: 
            self._t[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm: self._update_util(v*2, tl, tm, pos, new_val)
            else: self._update_util(v*2+1, tm+1, tr, pos, new_val)
            self._t[v] = self._t[v*2] + self._t[v*2+1]

    def sum(self, l, r):
        return self._sum_util(1 , 0 , self._n - 1 , l , r)
    
    def update(self, pos, new_val):
        self._update_util(1 , 0 , self._n - 1 , pos , new_val)
    
    def add(self, pos, change):
        value = self._sum(pos , pos)
        self._update_util(1 , 0 , self._n - 1 , pos , value + change)