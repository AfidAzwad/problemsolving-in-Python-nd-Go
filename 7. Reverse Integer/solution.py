def reverse(x):
    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1  # Define 32-bit integer range

    result = 0
    negative = x < 0
    x = abs(x)

    while x != 0:
        digit = x % 10  # Get the last digit
        x //= 10  # Remove the last digit

        # Check for overflow before updating result
        if result > (INT_MAX - digit) // 10:
            return 0
        result = result * 10 + digit

    return -result if negative else result

s = -321
print(reverse(s))

