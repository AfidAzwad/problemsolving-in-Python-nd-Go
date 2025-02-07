from collections import Counter


def minWindow(s,t):
    L, R = 0, len(t)-1
    count_t = Counter(t)
    min_window = ''
    min_len = float('inf')

    while R < len(s):
        count_sub = Counter(s[L:R+1])

        # expand window if current window is not correct
        while R < len(s) and any(count_sub[key] < count_t[key] for key in count_t):
            R += 1
            if R < len(s):
                count_sub[s[R]] += 1

        # shrink window from the left while it still satisfies t
        while all(count_sub[key] >= count_t[key] for key in count_t):
            if (R-L+1) < min_len:
                min_window = s[L:R+1]
                min_len = R-L+1
            count_sub[s[L]] -= 1
            L += 1

    return min_window

s = "ABECODEBAC"
t = "ABC"
print(minWindow(s,t))
