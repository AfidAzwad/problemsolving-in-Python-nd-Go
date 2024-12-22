import re

def validPalindrome(s):
    if s == '':
        return True
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    L, R = 0, len(s)-1

    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1
    return True


s = '0P'
print(validPalindrome(s))
