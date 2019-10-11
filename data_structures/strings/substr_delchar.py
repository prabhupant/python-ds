# Python3 program to Find all combinations of string after deleting k characters
list = []


def findCombinations(str, temp, start, end, index, k):

    if (index == k):
        item = ''

        for j in range(k):
            item += temp[j]
        list.append(item)
        return

    i = start
    while(i <= end and end - i + 1 >= k - index):
        temp[index] = str[i]
        findCombinations(str, temp, i + 1,
                         end, index + 1, k)
        i += 1


# Driver Code
str = 'geeks'
k = 1
temp = [0]*(len(str)-k)
s, e = 0, len(str)-1

findCombinations(str, temp, s, e, 0, len(str)-k)
print(set(list))
