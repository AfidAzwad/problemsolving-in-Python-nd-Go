def IsPalindrome(string):
    L, R = 0, len(string)-1

    while L < R:
        if string[L] == string[R]:
            L += 1
            R -= 1
        else:
            return False
    return True

string = 'abba'
print(IsPalindrome(string))