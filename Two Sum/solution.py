def twoSum(self, nums, target):
    diffHasmap = {}  # value : index

    for index, value in enumerate(nums):
        diff = target - value
        if diff in diffHasmap:
            return [diffHasmap[diff], index]
        diffHasmap[value] = index
    return

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))

# Time Complexity: O(n)
# Space Complexity: O(n)
