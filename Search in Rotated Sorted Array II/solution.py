def search(nums,target):
    L, R = 0, len(nums) - 1

    while L<R:
        if target == nums[L] or target == nums[R]:
            return True
        if nums[L] > nums[R]:
            L += 1
        else:
            R -= 1
    return False

nums = [1,0,1,1,1]
target =0
print(search(nums,target))

# Time Complexity: O(n)
# Space Complexity: O(1)


def searchOptimized(nums,target):
    L, R = 0, len(nums) - 1

    while L <= R:
        mid = (L + R) // 2

        if nums[mid] == target:
            return True

        # duplicates
        if nums[L] == nums[mid] == nums[R]:
            L += 1
            R -= 1

        #left is sorted
        elif nums[L] <= nums[mid]:
            if nums[L] <= target < nums[mid]:
                R = mid-1
            else:
                L = mid+1
        # Right is sorted
        else:
            if nums[mid] < target <= nums[R]:
                L = mid+1
            else:
                R = mid-1
    return False

nums = [1,0,1,1,1]
target =0
print(searchOptimized(nums,target))

# Time Complexity: O(log n)
# Space Complexity: O(1)

# *************** Runtime : Beat 100% in LeetCode
