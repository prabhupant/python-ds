class Z_Algorithm():
    """
        return all occurences of string s in text, returns its indexes starting from zero
        delimeter should be charachter which will not occur neither is S nor in text
        by default its '$'
    """
    @staticmethod
    def find_occurrences(s:str , text:str , delimeter = '$'):
        return Z_Algorithm.z_function(s + delimeter + text , len(s))
    
    @staticmethod
    def z_function(text:str , size:int):
        l = 0
        r = 0
        z = [0] * len(text)
        for i in range(1 , len(text)):
            if i <= r:
                z[i] = min(r - i + 1 , z[i - l])
            while i + z[i] < len(text) and text[z[i]] == text[i + z[i]]:
                z[i] += 1
            
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        
        res = []
        for i in range(size , len(text)):
            if z[i] == size:
                res.append(i - size - 1)
        return res