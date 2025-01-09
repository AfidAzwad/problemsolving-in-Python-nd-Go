from collections import Counter

def intersect(nums1,nums2):
    """
    Finds the intersection of two arrays, allowing duplicate values.

    Time Complexity: O(n + m)
    Space Complexity: O(n), where n is the length of nums1
    """

    hashMap = Counter(nums1)
    result = []

    for value in nums2:
        if hashMap[value] > 0:
            result.append(value)
        hashMap[value] -= 1
    return result


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))  # Output should be [4,9]

# Note:
# - If the arrays are sorted, you can use a two-pointer approach.
# - TC: O(n log n + m log m) for sorting both arrays.
# - SC: O(1) if sorting is done in place.
# Use the two-pointer approach if space is limited or if the interviewer specifies that the arrays are sorted.

