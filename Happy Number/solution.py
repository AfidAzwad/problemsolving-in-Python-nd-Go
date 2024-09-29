def isHappy(n):
    if len(str(n)) == 1:
        return False
    if n == 1:
        return True

    def get_sum_of_squares(digits):
        total = sum(int(digit) ** 2 for digit in str(digits))
        return total

    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = get_sum_of_squares(n)

    return True

n = 2
print(isHappy(n))

# Time Complexity: O(logN) # the number of digits in a number is logarithmic relative to its value.
# Space Complexity: O(N)
