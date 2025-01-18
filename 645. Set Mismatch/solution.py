from collections import Counter

def findErrorNums(nums):

    """
    TC : O(n)
    SC : O(n)
    """
    # result = [0,0]
    # count = Counter(nums)
    #
    # for i in range(1,len(nums)+1):
    #     if count[i] == 2:
    #         result[0] = i
    #     if count[i] == 0:
    #         result[1] = i
    # return result

    """
    TC : O(n)
    SC : O(1)
    """
    result = [0, 0]

    # TC : O(n)
    # SC : O(1)
    result = [0, 0]

    # Mark numbers as visited by negating values
    for number in nums:  # O(n)
        number = abs(number)  # Ensure the number is positive
        nums[number - 1] = -nums[number - 1]  # Mark index as visited
        if nums[number - 1] > 0:  # If already visited, it's now positive and duplicate
            result[0] = number

    # Identify the missing number
    for i, number in enumerate(nums):  # O(n)
        if number > 0:  # If the number at index is still positive
            result[1] = i + 1  # This is the missing number
            return result

nums = [5,1,2,2,4]
print(findErrorNums(nums))
