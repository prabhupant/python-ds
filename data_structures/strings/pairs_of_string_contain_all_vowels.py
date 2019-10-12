'''
Question:
N strings numbered 1 throug N containing only lowercase vowels. i.e characters 'a', 'e', 'i', 'o', 'u'.
for each valid i string i is described by Di. there is another string 'M' made using concatenating the two strings
Di and Dj(i != j) in an arbitary order. A string 'M' is valid if it contains each lowercase vowel atleast once.
Output -> what is the total number of (unordered) pairs of strings such that they are valid string?

Time complexity:
to encode string: n (length of string)
to count combination: ~31**2 (or constant)

Reference:
Codechef
'''

def encode(s):
    code = 0
    for i in s:
        if i == 'a':
            code |= 1
        elif i == 'e':
            code |= 2
        elif i == 'i':
            code |= 4
        elif i == 'o':
            code |= 8
        else:
            code |= 16
    return code


if __name__=='__main__':
    n_strings = int(input('Enter number of strings\n'))

    frequency_31 = [0]*32
    print('Enter {} strings'.format(n_strings))
    while n_strings:
        s = input()
        frequency_31[encode(s)] += 1
        n_strings -= 1

    count = 0
    for i in range(1, 31):
        for j in range(i+1, 32):
            if i|j is 31:
                count += frequency_31[i] * frequency_31[j]

    count += int((frequency_31[31] * (frequency_31[31] - 1))/ 2)

    print('Total number of valid strings: ', count)



        
