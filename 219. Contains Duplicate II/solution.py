def containsNearbyDuplicate(nums, k):
    hashTable = {}

    for i in range(len(nums)):
        if nums[i] in hashTable:
            if abs(hashTable[nums[i]] - i) <= k:
                return True
        hashTable[nums[i]] = i

    return False

nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))

# Time Complexity: O(n)
# Space Complexity: O(n)
