def lengthOfLongestSubstring(s):
    windowSet = set()
    left = 0
    size = 0

    for right in range(len(s)):
        while s[right] in windowSet:
            windowSet.remove(s[left])
            left += 1
        windowSet.add(s[right])
        size = max(size, right - left + 1)
    return size


s = "abcabcbb"
print(lengthOfLongestSubstring(s))

