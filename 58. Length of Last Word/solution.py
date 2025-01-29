def lengthOfLastWord(s):
    # """ With TC : O(n) and SC : O(n)"""
    # return len(s.split()[::-1][0])

    """ With TC : O(n) and SC : O(1)"""
    R = len(s)-1

    while R >= 0 and s[R] == ' ':
        R -= 1
    length = 0

    while R >= 0 and s[R] != ' ':
        length += 1
        R -= 1
    return length

s = "r   rr  "
print(lengthOfLastWord(s))