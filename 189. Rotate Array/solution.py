def rotate(nums, k):
    """
    Rotates an array 'nums' in place by 'k' steps to the right using the reversal algorithm.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    # Handle cases where k >= len(nums) and avoid unnecessary rotations
    k = k % len(nums)
    if k == 0 or not nums:  # No rotation needed for k = 0 or empty list
        return nums

    # Reverse the entire array
    L, R = 0, len(nums) - 1
    while L < R:
        nums[L], nums[R] = nums[R], nums[L]
        L += 1
        R -= 1

    # Reverse the first k elements
    L, R = 0, k - 1
    while L < R:
        nums[L], nums[R] = nums[R], nums[L]
        L += 1
        R -= 1

    # Reverse the remaining n-k elements
    L, R = k, len(nums) - 1
    while L < R:
        nums[L], nums[R] = nums[R], nums[L]
        L += 1
        R -= 1

    return nums


nums = [1, 2, 3, 4, 5, 6]
k = 3
print(rotate(nums, k))  # Output should be [4, 5, 6, 1, 2, 3]
