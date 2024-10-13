def removeDuplicates(nums):
    count = 1
    i = 1

    while i < len(nums):
        if nums[i] == nums[i - 1]:
            count += 1
            if count > 2:
                nums.pop(i)
                i -= 1  # Stay on the current index to check again
        else:
            count = 1  # Reset count for new element
        i += 1
    return len(nums)

nums = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
print(removeDuplicates(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)
