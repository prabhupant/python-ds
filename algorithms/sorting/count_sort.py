def Count_Sort(arr): 
  
    temp = count = [0 for i in range(256)] 
     
    result = ["" for _ in arr]  
    for i in arr: 
        count[ord(i)] += 1
  
    for i in range(256): 
        count[i] += count[i-1] 
  
    for i in range(len(arr)): 
        temp[count[ord(arr[i])]-1] = arr[i] 
        count[ord(arr[i])] -= 1
   
    for i in range(len(arr)): 
        result[i] = output[i] 
    return result  
