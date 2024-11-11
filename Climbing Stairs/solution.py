def climbStairs(n):
    one, two = 1, 1

    for i in range(n-1):
        one, two = one + two, one

    return one

n = 3
print(climbStairs(n))

# Here we are doing DP Bottom-Up approach
# Time Complexity: O(n)
# Space Complexity: O(1)
