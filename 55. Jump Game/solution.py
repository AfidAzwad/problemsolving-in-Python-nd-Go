def canJump(nums):
    goal = len(nums) - 1

    for i in range(goal, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0

# nums = [2,3,1,1,4]
# nums = [0]
nums = [2,5,0,0]
print(canJump(nums))

"""
    Time Complexity (TC): O(n)
    - We iterate through the array once in reverse order, so the complexity is linear with respect to the size of the array.

    Space Complexity (SC): O(1)
    - No additional data structures are used; only a few variables are maintained.
"""
