def isUgly(n):
    # Negative numbers and zero are not considered ugly
    if n <= 0:
        return False

    for prime in [2, 3, 5]:
        # Continuously divide n by the prime factor while it is divisible
        while n % prime == 0:
            n = n // prime

    # If the remaining value of n is 1, it's an ugly number
    return n == 1

n = 4
print(isUgly(n))

"""
Time Complexity: O(log(n))
- For each prime factor(2, 3, 5), the number n is divided repeatedly until it is no longer divisible.
- The maximum number of divisions for a prime factor is proportional to the logarithm of n in base 2 (worst case).

Space Complexity: O(1)
- The algorithm uses a constant amount of space, with no additional data structures or recursion.
"""