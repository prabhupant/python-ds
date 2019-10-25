#print all permutations of string using backtracking



def permute(text):
    _permute(list(text),0,len(text)-1)


def _permute(text,start,end):
    count =1
    if start == end:
        count +=1
        print(''.join(text))
    #print(count)
    for i in range(start,end+1):
        text[start],text[i] = text[i],text[start]
        _permute(text,start+1,end)
        text[start],text[i] = text[i],text[start]
        
           
            


    

    


permute("abc")

