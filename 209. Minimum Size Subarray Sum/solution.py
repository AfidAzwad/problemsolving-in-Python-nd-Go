def minSubArrayLen(nums, target):
    L, total = 0, 0
    result = float('inf')

    for i in range(len(nums)):
        total += nums[i]
        while total >= target:
            result = min(result, i - L + 1)  # update result if current window is smaller
            total -= nums[L]
            L += 1
    return 0 if result == float('inf') else result

target = 7
nums = [4,1,0,7,1,7]
print(minSubArrayLen(nums, target))

# Time Complexity: O(n)
# Space Complexity: O(n)
