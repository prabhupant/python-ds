#find the number of adjacent pairs of vowels in a string
#python3

def isvowel(c):
    
    if c in ['a', 'e', 'i', 'o', 'u']: 
        return True
    else:  
        return False
  

def adjacentpairs(s):
    n=len(s)
  
    count = 0
    for i in range(n): 
  
        
        if (isvowel(s[i]) and isvowel(s[i + 1])): 
            count += 1
  
    return count

s=input("enter string")
print (adjacentpairs(s),"is the number of adjacent pairs of vowels")
  
