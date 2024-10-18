def judgeSquareSum(c):

    for a in range(int(c**0.5) + 1):  # a can be at most sqrt(c)
        b_square = c - a * a
        b = int(b_square**0.5)

        if b * b == b_square:
            return True

    return False

c = 3
print(judgeSquareSum(c))

# Time Complexity: O(sqrt(c))
# Space Complexity: O(1)
