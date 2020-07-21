def longest_palindromic_substring_dp(s):

    string = [[False for _ in range(len(s))] for _ in range(len(s))]

    max_palindrome = ""

    for i in range(len(s))[::-1]:
        for j in range(i, len(s)):
            # if j - 1 < 3, then there is one or two characters between these
            # two positions, implying that if s[i] == s[j]
            # then that small string is a palindrome
            # We check if the above cases is valid or i
            # they are larger, we use DP to check the substring
            # in between j and i
            string[i][j] = s[i] == s[j] and (j - i < 3 or string[i+1][j-1])
            if string[i][j] and j - i + 1 > len(max_palindrome):
                max_palindrome = s[i:j+1]

    return max_palindrome


def longest_palindromic_substring_expansion(s):
    max_palindrome = ""

    for i in range(len(s) * 2 - 1):
        if i % 2 == 0:
            # This is when you are "on" an actual character
            # o = offset, ind = current character
            o = 0
            ind = i // 2
            while ind + o < len(s) and ind - o >= 0:
                if s[ind + o] != s[ind - o]:
                    break
                if ind + o - (ind - o) + 1 > len(max_palindrome):
                    max_palindrome = s[ind-o:ind+o + 1]
                o += 1
        else:
            # This is when you are "in the middle of" two characters
            # o = offset, sind = start char, eind = end char
            o = 0
            sind = i // 2
            eind = i // 2 + 1
            while sind - o >= 0 and eind + o < len(s):
                if s[sind - o] != s[eind + o]:
                    break
                if eind + o - (sind - o) + 1 > len(max_palindrome):
                    max_palindrome = s[sind - o:eind + o + 1]
                o += 1

    return max_palindrome


# TESTING
input_string = "abbbacdcaacdca"

ans_DP = longest_palindromic_substring_dp(input_string)
ans_expansion = longest_palindromic_substring_expansion(input_string)
print("DP Solution: {}, Expansion Solution: {}".format(ans_DP, ans_expansion))
