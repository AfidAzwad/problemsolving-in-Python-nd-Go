def threeSum(nums):
    triplets = []

    # Sorting the array takes O(n log n) time
    nums.sort()

    for index, value in enumerate(nums):
        # Skip duplicate elements to avoid duplicate triplets
        if index > 0 and value == nums[index - 1]:
            continue

        left = index + 1
        right = len(nums) - 1

        # Two-pointer approach
        while left < right:
            total = value + nums[left] + nums[right]

            if total < 0:
                left += 1  # Move left pointer to increase the sum
            elif total > 0:
                right -= 1  # Move right pointer to decrease the sum
            else:
                # Found a valid triplet
                triplets.append([value, nums[left], nums[right]])

                # Skip duplicate elements to avoid duplicate triplets
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers after storing a valid triplet
                left += 1
                right -= 1

    return triplets


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]

# Time Complexity Analysis:
# 1. Sorting the array takes O(n log n).
# 2. The main loop runs O(n) times.
# 3. Inside the loop, the two-pointer approach runs in O(n).
# 4. Thus, the overall time complexity is O(n log n) + O(n^2) ≈ O(n^2).

# Space Complexity Analysis:
# 1. Sorting is done in-place, so it requires O(1) extra space.
# 2. The result list `triplets` stores valid triplets, which in the worst case can be O(n^2).
# 3. No extra data structures are used apart from the output list.
# 4. Thus, the overall space complexity is O(n) to O(n^2) (depending on the number of valid triplets).
