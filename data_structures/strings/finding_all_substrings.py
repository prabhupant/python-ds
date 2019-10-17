'''
Question : Print and Count all the substrings of a given string.
Sample Input : hello
Sample Output : ['h', 'he', 'hel', 'hell', 'hello', 'e', 'el', 'ell', 'ello', 'l', 'll', 'llo', 'l', 'lo', 'o']
15
Source : Hackerrank'''

def finding_substrings(string):
  
    # Get all substrings of string and store them in an empty list
    list =[]
    count=0
    for i in range(len(string)):
        for j in range(i+1,(len(string)+1)):
            list.append(string[i:j])

            count=count+1
        
    # printing result  
    print(list)
    print(count)

#driver code
string = input("enter string: ")
finding_substrings(string)

