class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        l=[]
        i=0
        while(i!=len(A[0])):
            x=[]
            j=0
            while(j<len(A)):
                x.append(A[j][i])
                j+=1
            if(x!=[]):
                l.append(x)
            i+=1
        return(l)
