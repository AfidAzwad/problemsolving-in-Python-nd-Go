class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMode(root):
    current_count = 0
    current_value = None
    max_count = 0
    mode = []

    def inorder(node):
        nonlocal current_count, current_value, max_count, mode

        if node is None:
            return

        inorder(node.left)

        # Check value
        if node.val == current_value:
            current_count += 1
        else:
            current_count = 1
            current_value = node.val

        # Check count
        if current_count > max_count:
            max_count = current_count
            mode = [current_value]
        elif current_count == max_count:
            mode.append(current_value)

        inorder(node.right)

    inorder(root)
    return mode

# Example tree: [1, null, 2]
root = TreeNode(1)
root.right = TreeNode(2)

# Find and print the mode(s)
print(findMode(root))  # Output: [1, 2]

# Time complexity: O(n), where n is the number of nodes in the tree.
# Space complexity: O(h), where h is the height of the tree, due to the recursion stack.
