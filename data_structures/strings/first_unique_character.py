from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:    
        seen = Counter(s)
        
        for ch, i in seen.items():
            if i == 1:
                return s.index(ch)

        return -1