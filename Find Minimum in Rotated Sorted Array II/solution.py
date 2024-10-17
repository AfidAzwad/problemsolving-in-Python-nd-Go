def findMin(nums):
    L, R = 0, len(nums) - 1

    while L<R:
        if nums[L] > nums[R]:
            L += 1
        else:
            R -= 1
    return nums[L]

nums = [3,3,1,3]
print(findMin(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)


def findMinOptimized(nums):
    L, R = 0, len(nums) - 1

    while L < R:
        mid = (L + R) // 2

        if nums[mid] > nums[R]:
            L = mid + 1
        elif nums[mid] == nums[R] == nums[L]:
            L += 1
            R -= 1
        else:
            R = mid
    return nums[L]

nums = [3, 3, 3, 1, 3, 3, 3, 3, 3]
print(findMinOptimized(nums))

# Time Complexity: O(log n)
# Space Complexity: O(1)
