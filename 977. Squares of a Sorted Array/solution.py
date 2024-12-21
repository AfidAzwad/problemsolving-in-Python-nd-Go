def sortedSquares(nums):
    L, R = 0, len(nums) - 1
    result = [0] * len(nums)  # Preallocate the result list
    position = len(nums) - 1  # Start filling from the last position

    while L <= R:
        left_square = nums[L] ** 2
        right_square = nums[R] ** 2

        if right_square > left_square:
            result[position] = right_square
            R -= 1
        else:
            result[position] = left_square
            L += 1

        position -= 1  # Move to the next position

    return result


nums = [-4,-1,0,3,10]
print(sortedSquares(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)
