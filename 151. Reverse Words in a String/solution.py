def reverseWords(s):
    s = s.strip()
    res = ''
    L = R = len(s) - 1

    while L >= 0:
        if s[L] == ' ':
            res += s[L + 1:R + 1] + ' '
            while L >= 0 and s[L] == ' ':
                L -= 1
            R = L
        else:
            L -= 1
    res += s[L + 1:R + 1]
    return res

s = "the sky is blue"
print(reverseWords(s))  # Output: "blue is sky the"

# TC : O(n)+O(n)=O(n)
# SC : O(n)

""" built in approach """
def reverseWords(s):
    return ' '.join(s.strip().split()[::-1])

s = "the sky     is blue"
print(reverseWords(s))  # Output: "blue is sky the"

"""
Time Complexity (TC):
1. `strip()`: O(n), where n is the length of the string.
2. `split()`: O(n) for splitting the string into words.
3. `[::-1]`: O(k) for reversing the list of k words (k ≤ n).
4. `' '.join()`: O(n) for joining the words into a single string.
Overall TC: O(n + k) ≈ O(n)

Space Complexity (SC):
1. `strip()`: O(n) for creating a trimmed copy of the string.
2. `split()`: O(k) for storing the words in a list.
3. `[::-1]`: O(k) for the reversed list.
4. `' '.join()`: O(n) for the output string.
Overall SCC: O(n + k) ≈ O(n)
"""

''' Note : As strings are immutable in Python so it's not possible to modify in-place with O(1) space complexity '''