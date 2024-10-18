def findIntersection(nums):
    if len(nums) < 2:
        return []

    # Start with the first array as the initial intersection set
    common_values = set(nums[0])

    for i in range(1, len(nums)):
        # Intersect the current set of common values with the next array
        common_values &= set(nums[i])

        if not common_values:
            return []

    return list(common_values)

# Test with sample data
nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
print(findIntersection(nums))

# Time Complexity: O(n1 + n2 + ... + nk) + O(log n) , where n is the size of the intersection.
# Space Complexity: O(min(n1, n2, ... ,nk))

# Intersection operations: As before, the time complexity for intersection is O(n1 + n2 + ... + nk)
# Sorting: Sorting the final list of common values has a time complexity of O(log n)