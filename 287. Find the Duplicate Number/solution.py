def findDuplicate(nums):
    # seen = set()
    # for i in nums:
    #     if i in seen:
    #         return i
    #     else:
    #         seen.add(i)
    # TC and SC : O(n) and O(n)

    # Step 1: Detect the cycle
    # as nums.length == n + 1 so we have 1 extra index than max value of this array
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Step 2: Find the value
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

    # TC and SC : O(n) and O(1)

nums = [3, 1, 3, 4, 2]
print(findDuplicate(nums))
