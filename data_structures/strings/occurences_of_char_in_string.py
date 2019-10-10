'''
Cool and pythonic way of counting the occurrences of all characters in a string.
'''

string = input("Enter Your string")
count_dict = {i:string.count(i) for i in string}

for i in count_dict.items():
  print("Count of '{}' in the string '{}' is {}".format(i[0],string,i[1]))
