from collections import Counter

def intersect(nums1,nums2):
    result = set(nums1) & set(nums2)
    return list(result)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))  # Output should be [4,9]

# Time Complexity (TC): O(n + m)
# - Converting both lists to sets takes O(n) and O(m), respectively.
# - Finding the intersection between two sets is O(min(n, m)).

# Space Complexity (SC): O(n + m)
# - Additional space is required for two sets and the resulting list.

# ⚠️ If duplicates need to be considered in the intersection:
# - Use a hashmap or Counter for one of the arrays.
# - Compare the counts to ensure duplicate matches.

