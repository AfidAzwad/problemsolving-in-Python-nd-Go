def evalRPN(tokens):
    stack = []
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y)  # Truncate towards zero
    }

    for token in tokens:
        '1st option'
        if token in ['+', '-', '*', '/']:
            if stack:
                b, a = stack.pop(), stack.pop()
                stack.append(operations[token](a,b))
        else:
            stack.append(int(token))

        '2nd option'
        # if token == "+":
        #     stack.append(stack.pop() + stack.pop())
        # elif token == "-":
        #     b, a = stack.pop(), stack.pop()
        #     stack.append(a - b)
        # elif token == "*":
        #     stack.append(stack.pop() * stack.pop())
        # elif token == "/":
        #     b, a = stack.pop(), stack.pop()
        #     stack.append(int(a/b))
        # else:
        #     stack.append(int(token))

    return stack[0]

tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))

"""
Time Complexity (TC): O(n)

Space Complexity (SC): O(n)

"""