def longestConsecutive(nums):
    nums = sorted(set(nums))  # O(nlogn)
    count = 1
    longest = 0

    for i in range(0, len(nums)):  # O(n)
        if nums[i] in nums and nums[i]+1 in nums:
            count += 1
        else:
            longest = max(longest, count)
            count = 1
    return longest

nums = [100,4,200,1,3,2, 21,22,23,24,25]
# print(longestConsecutive(nums))

# overall time and space is : O(nlogn) and O(n) and result will be 'Time Limit Exceeded' for large lists


########## optimized solution ###########

def longestConsecutiveOptimized(nums):
    nums = set(nums) # duplicates removed O(n)
    longest = 0

    for i in nums: # O(n)
        if i-1 not in nums:
            current = i
            count = 1
            print('current: ', current)
            while current+1 in nums:
                current += 1
                count += 1
                print('current while: ', current)
            longest = max(longest, count)
    return longest

nums = [100,4,200,1,3,2,21,22,23,24,25,26,27]
print(longestConsecutiveOptimized(nums))

# overall time and space is : O(n) and O(n)