# find out the product of 3 largest elements in list


import sys

def product(lst):
    maximum = -(sys.maxsize-1)
    for i in range(0,len(lst)-2):
        for j in range(i+1,len(lst)-1):
            for k in range(j+1,len(lst)):
                maximum = max(maximum,lst[i]*lst[j]*lst[k])

    print(maximum)
                    
        
        
        


product([-10,-10,5,10,2])
