def jump(nums):
    L = R = count = 0

    while R < len(nums) - 1:
        # Initialize the farthest position that can be reached in the current jump window
        longest_jump = 0

        # Explore all indices within the current jump window (from L to R)
        for i in range(L, R + 1):
            # Update the farthest position that can be reached
            longest_jump = max(longest_jump, i + nums[i])

        # Update the pointers for the next jump window
        L = R + 1  # The left pointer moves to the next position after the current window
        R = longest_jump  # The right pointer moves to the farthest reachable position
        count += 1

    return count

nums = [3,4,3,2,5,4,3]
print(jump(nums))

"""
Approach:
1. **Sliding Window Technique**: This problem uses a sliding window approach to explore the range of indices reachable in the current jump window.
2. **Greedy Method**: At each step, the algorithm calculates the farthest position (`longest_jump`) that can be reached within the current window.
3. **Jump Count**: The `count` variable tracks the number of jumps required to reach the end of the array.

Time Complexity (TC): O(n)
- In each iteration of the outer `while` loop, the inner `for` loop iterates over the elements of the current jump window.
- Each element is processed at most once, so the total complexity is O(n).

Space Complexity (SC): O(1)
- The algorithm uses a constant amount of extra space, regardless of the size of the input array.

"""
