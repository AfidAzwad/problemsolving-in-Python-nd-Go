def longestPalindromeSubseq(s):

    result = ''

    for i in range(len(s)):
        # odd-length palindromes
        L, R = i, i
        while L >= 0 and R < len(s) and s[L] == s[R]:
            if (R - L + 1) > len(result):
                result = s[L:R+1]
            L -= 1
            R += 1

        # even-length palindromes
        L,R = i, i+1
        while L >= 0 and R < len(s) and s[L] == s[R]:
            if (R - L + 1) > len(result):
                result = s[L:R+1]
            L -= 1
            R += 1

    # rest_of_string = list(s.replace(result, "", 1))
    # while result[0] in rest_of_string:
    #     result += result[0]
    #     rest_of_string.remove(result[0])

    return len(result)

s = 'abcabcabcabc'
print(longestPalindromeSubseq(s))

# overall time and space is : O(n) and O(n)