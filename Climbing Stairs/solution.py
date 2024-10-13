def climbStairs(n):
    one, two = 1, 1

    for i in range(n-1):
        temp = one
        one = one + two
        two = temp

    return one

n = 5
print(climbStairs(n))

# Here we are doing DP Bottom-Up approach
# Time Complexity: O(n)
# Space Complexity: O(1)
