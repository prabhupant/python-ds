class ZAlgorithm:
    """
        return all occurrences of string s in text, returns its indexes starting from zero
        delimiter should be character which will not occur neither is S nor in text
        by default its '$'
    """
    @staticmethod
    def find_occurrences(s: str, text: str, delimiter='$'):
        return ZAlgorithm.z_function(s + delimiter + text, len(s))
    
    @staticmethod
    def z_function(text: str, size: int):
        left = 0
        right = 0
        z = [0] * len(text)
        for i in range(1, len(text)):
            if i <= right:
                z[i] = min(right - i + 1, z[i - left])
            while i + z[i] < len(text) and text[z[i]] == text[i + z[i]]:
                z[i] += 1
            
            if i + z[i] - 1 > right:
                left = i
                right = i + z[i] - 1
        
        res = []
        for i in range(size, len(text)):
            if z[i] == size:
                res.append(i - size - 1)
        return res
