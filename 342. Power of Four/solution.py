def isPowerOfFour(n):
    while n % 4 == 0:
        n //= 4
    return n == 1

n = 15
print(isPowerOfFour(n))

# Time Complexity (TC): O(log4(n))
# - In each iteration of the while loop, the number is divided by 4.
# - The number of iterations is proportional to the number of times n can be divided by 4, which is log base 4 of n.

# Space Complexity (SC): O(1)
# - The algorithm only uses a constant amount of extra space for the loop and variables.


''' Without Loops'''

def isPowerOfFour(n):
    # Check if n is a positive power of two and satisfies (n-1) % 3 == 0
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

n = 16
print(isPowerOfFour(n))  # Output: True

n = 9
print(isPowerOfFour(n))  # Output: False

# Time Complexity (TC): O(1)
# - All operations (bitwise, modulo) are constant time.

# Space Complexity (SC): O(1)
# - No extra space is used.
