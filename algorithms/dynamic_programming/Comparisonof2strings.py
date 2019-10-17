'''
Question : To find the equality of 2 strings by edit distance algorithm
Sample Input : str1 , str2
Sample Output : 39 , Strings are almost equal

Source : Geeksforgeeks'''

def editDistDP(str1, str2 , m , n):

    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],    dp[i - 1][j],     dp[i - 1][j - 1])

    return dp[m][n]

if __name__ == '__main__':
    str1 = "https://www.dell.com/en-us/shop/dell-laptops/inspiron-11-3000-laptop/spd/inspiron-11-3180-laptop"
    str2 = "https://www.dell.com/en-us/member/shop/laptops/11-2-in-1/spd/inspiron-11-3195-2-in-1-laptop"
    len1 = editDistDP(str1 ,str2 ,len(str1) , len(str2))
    if len1 <40: #limit can be adjusted based on the use-case
        message= "Strings are almost equal"
    else:
        message = "Strings are not equal"
    print(len1)
    print(message)