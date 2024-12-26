def reverseString(s):
    L, R = 0, len(s) - 1

    while L < R:
        s[L], s[R] = s[R], s[L]
        L += 1
        R -= 1

    return s


s = ["h","e","l","l","o"]
print(reverseString(s))

# Time Complexity: O(n)
# Space Complexity: O(1)
