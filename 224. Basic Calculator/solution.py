def calculate(s):
    stack = []  # Stack to handle parentheses and intermediate results
    curr = res = 0  # `curr` holds the current number, `res` holds the evaluated result so far
    sign = 1

    for char in s:
        if char.isdigit():
            # If the character is a digit, update `curr` by shifting the previous value
            curr = curr * 10 + int(char)
        elif char in ['+', '-']:
            # If an operator is found, apply the previous number with its sign
            res += sign * curr
            sign = 1 if char == '+' else -1
            curr = 0
        elif char == '(':
            # Push the current result and sign onto the stack (for later computation)
            stack.append(res)
            stack.append(sign)
            # Reset for the new sub-expression inside parentheses
            sign = 1
            res = 0
        elif char == ')':
            # Evaluate the expression within parentheses
            res += sign * curr  # Apply the last pending number
            res *= stack.pop()  # Multiply by sign before parentheses
            res += stack.pop()  # Add the result before the parentheses

            curr = 0

    return res + sign * curr

s = '(1+(4+5+2)-3)+(6+8)'
print(calculate(s))

"""
# Time Complexity Analysis:
- We iterate through the input string `s` exactly once, making the time complexity **O(N)**,
  where `N` is the length of the input string.

# Space Complexity Analysis:
- The stack stores at most **O(N)** elements in the worst case (when handling deeply nested parentheses).
- Other variables take **O(1)** space.
- Overall, the space complexity is **O(N)** in the worst case.
"""
