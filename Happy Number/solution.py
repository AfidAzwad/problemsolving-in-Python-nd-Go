def isHappy(n):
    if n == 1:
        return True

    def get_sum_of_squares(n):
        output = 0
        while n:
            digit = n % 10
            output += digit ** 2
            n = n // 10
        return output

    seen = set()

    while n not in seen:
        seen.add(n)
        n = get_sum_of_squares(n)
        if n == 1:
            return True

    return False

n = 2
print(isHappy(n))

# Time Complexity: O(logN) # the number of digits in a number is logarithmic relative to its value.
# Space Complexity: O(N)
