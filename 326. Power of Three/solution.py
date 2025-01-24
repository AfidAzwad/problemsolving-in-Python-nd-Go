def isPowerOfThree(n):
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3
    return n == 1

n = 81
print(isPowerOfThree(n))

# Time Complexity (TC): O(log3(n))
# - In each iteration of the while loop, the number is divided by 3.
# - The number of iterations is proportional to the number of times n can be divided by 3, which is log base 3 of n.

# Space Complexity (SC): O(1)
# - The algorithm only uses a constant amount of extra space for the loop and variables.