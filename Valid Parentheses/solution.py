def is_valid_parentheses(s):
    parenthesesMap = {')':'(', '}':'{', ']':'[' }

    stack = []

    for parantheses in s:
        if parantheses in parenthesesMap:  # if Closing bracket
            if not stack or stack[-1] != parenthesesMap[parantheses]:
                return False
            stack.pop()
        else:
            stack.append(parantheses)

    return len(stack) == 0  # Stack should be empty if valid

s = '[{})][]({[]})'
print(is_valid_parentheses(s))