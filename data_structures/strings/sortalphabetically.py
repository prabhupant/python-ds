'''
Question : Sort a string in alphabetical order(numbers followed by strings) in case of bigger strings
Sample Input : hel3lo41o
Sample Output : 134ehlloo

Source : ***'''
def sort(string1):
    string_sort =''.join(sorted(string1))
    print(string_sort)
if __name__ == '__main__':
    sort("hel3lo41 girl")