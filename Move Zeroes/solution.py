def moveZeroes(nums):
    L, R = 0, 1

    while R < len(nums):
        if nums[L] != 0:
            L += 1
            R += 1
        elif nums[R] != 0:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R += 1
        else:
            R += 1
    return nums

nums = [0]

print(moveZeroes(nums))