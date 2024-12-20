def removeDuplicates(nums):
    L, R = 0, 1
    k = 1

    while R < len(nums):
        if nums[R] != nums[L]:
            L += 1
            nums[L] = nums[R]
            R += 1
            k += 1
        else:
            R += 1

    return L+1

nums = [1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]
print(removeDuplicates(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)
