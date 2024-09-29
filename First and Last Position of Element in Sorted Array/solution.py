def searchRange(nums, target):

    # with Binary Search O(logN)
    def BinarySearch(nums, target, leftMost):
        L, R = 0, len(nums) - 1
        i = -1
        while L <= R:
            mid = (L + R) // 2
            if target > nums[mid]:
                L = mid + 1
            elif target < nums[mid]:
                R = mid - 1
            else:
                i = mid
                if leftMost:
                    R = mid - 1
                else:
                   L = mid + 1
        return i

    leftMost = BinarySearch(nums, target, True)
    rightMost = BinarySearch(nums, target, False)

    return [leftMost, rightMost]

nums = [5,7,8,8,8,10]
target = 8
print(searchRange(nums,target))

# Time Complexity: O(logN)
# Space Complexity: O(n)
