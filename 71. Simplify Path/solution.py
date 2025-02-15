def simplifyPath(path):
    stack = []
    current = ''

    for char in path + '/':
        if char == '/':
            if current == '..':
                if stack:
                    stack.pop()
            elif current and current != '.':
                stack.append(current)
            current = ''
        else:
            current += char

    return '/' + '/'.join(stack)


path = "/a/b/c//d//././/.."
print(simplifyPath(path))

"""
- **Time complexity:**  
    O(n), where n is the length of the input `path`.
  - We traverse the path once (`O(n)`) and perform `push`/`pop` operations on the stack, which take `O(1)`.

- **Space complexity:**  
  O(n) in the worst case, where all directories are stored in the stack.
"""
