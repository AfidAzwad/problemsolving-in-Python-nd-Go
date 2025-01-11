from collections import Counter, defaultdict

def wordSubsets(words1, words2):
    result = []
    max_char_freq = defaultdict(int)

    # Step 1: Build count_word2 to get the maximum required frequency for each character from words2
    # TC for this step: O(m * k), where m = len(words2), k = average length of words
    # SC for this step: O(1) for count_word2, as it only stores at most 26 characters
    for word in words2:
        word_count = Counter(word)
        for key, value in word_count.items():
            max_char_freq[key] = max(value, max_char_freq.get(key, 0))

    # Step 2: Check each word in words1 to see if it satisfies the required character frequencies
    # TC for this step: O(n * k), where n = len(words1), k = average length of words
    # SC for this step: O(n) for the result list, in the worst case if all words are universal
    for word in words1:
        word_count = Counter(word)
        if all(word_count[key] >= value for key, value in max_char_freq.items()):
            result.append(word)

    # Final TC: O((m + n) * k), where m = len(words2), n = len(words1), k = average length of words
    # Final SC: O(n + k), where n is the size of the result list and k is the character count storage
    return result

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]  # words2 could have more complex strings like ["ee", "oo"]
print(wordSubsets(words1, words2))  # Output: ['facebook', 'google', 'leetcode']

