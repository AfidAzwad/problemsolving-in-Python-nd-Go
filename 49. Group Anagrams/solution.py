from collections import defaultdict


def groupAnagrams(strs):
    hashMap = defaultdict(list)

    for s in strs:
        sortedStr = ''.join(sorted(s))  # Sort each string
        hashMap[sortedStr].append(s)  # Append directly since defaultdict initializes lists

    return list(hashMap.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

"""
Time Complexity (TC): O(n * k log k)
- Sorting each string takes O(k log k), where k is the length of the string.
- Iterating over n strings gives an overall complexity of O(n * k log k).

Space Complexity (SC): O(n * k)
- The hashmap stores n keys (one per unique anagram group) with values as lists of strings.
- Each string takes O(k) space, leading to an overall space complexity of O(n * k).
"""
