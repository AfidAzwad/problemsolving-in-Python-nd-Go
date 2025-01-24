def wordPattern(pattern, s):
    words = s.split(" ")
    if len(pattern) != len(words):
        return False
    charDict = {}
    wordDict = {}

    for char, word in zip(pattern, words):
        if char in charDict and charDict[char] != word:
            return False
        if word in wordDict and wordDict[word] != char:
            return False
        charDict[char] = word
        wordDict[word] = char
    return True


pattern = "abba"
s = "dog cat cat ttt"
print(wordPattern(pattern, s))

"""
    TC: O(n)
    - Splitting the string `s` into words takes O(m), where m is the length of the string `s`.
    - The loop iterates over the pattern and words simultaneously, which is O(n), where n is the length of the pattern.
    - Since the number of words in `s` matches the length of the pattern, the dominant complexity is O(n).

    SC: O(n)
    - Two dictionaries (`charDict` and `wordDict`) are used to store mappings of characters to words and vice versa.
    - In the worst case, both dictionaries store all characters and words, resulting in O(n) space usage.
"""
