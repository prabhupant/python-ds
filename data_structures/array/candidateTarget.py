# Return the sublist of numbers in array which will return the target sum

def candidate_target(candidates, target,result =[]):
    if sum(result) == target:
        print(result)
        
    for i in range(len(candidates)):
        n = candidates[i]
        lst1 = candidates[i+1:]
        candidate_target(lst1, target, result + [n]) 

    

candidate_target([2,3,6,7],9)



