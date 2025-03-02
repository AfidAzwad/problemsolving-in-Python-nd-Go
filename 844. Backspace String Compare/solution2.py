def backspaceCompare(s,t):
    valid_s = []
    valid_t = []

    index_s, index_t = 0,0

    while index_s < len(s) or index_t < len(t):
        if index_s < len(s):
            if s[index_s] == '#':
                if valid_s: valid_s.pop()
            else:
                valid_s.append(s[index_s])
        if index_t < len(t):
            if t[index_t] == '#':
                if valid_t: valid_t.pop()
            else:
                valid_t.append(t[index_t])
        index_s +=1
        index_t +=1
    return valid_s == valid_t

s = "xywrrmp"
t = "xywrrmu#p"
print(backspaceCompare(s,t))

# TC and SC both : O(N+M)
