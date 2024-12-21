def twoSum(nums, target):
    L, R = 0, len(nums)-1

    while L < R:
        total = nums[L] + nums[R]
        if total == target:
            return L+1, R+1
        elif total > target:
            R -= 1
        elif total < target:
            L += 1

nums = [2,7,11,15,16,17,18,19]
target = 31
print(twoSum(nums,target))

# Time Complexity: O(n)
# Space Complexity: O(n)
