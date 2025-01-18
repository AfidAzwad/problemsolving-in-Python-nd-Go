def isSubsequence(s, t):
    L, R = 0, 0

    while L < len(s) and R < len(t):  # Loop runs at most len(t) times
        if s[L] == t[R]:
            L += 1
        R += 1

    return L == len(s)


s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))

# Time Complexity:
# - The while loop runs as long as both L < len(s) and R < len(t).
# - In the worst case, R iterates through all characters in t, resulting in O(len(t)).
# - Each comparison within the loop is O(1).
# - Overall time complexity: O(len(t)).

# Space Complexity:
# - The algorithm uses only a few variables (L, R), which take constant space.
# - No additional data structures are used.
# - Overall space complexity: O(1).