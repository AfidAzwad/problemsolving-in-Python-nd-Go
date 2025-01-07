# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Manually constructing the BST from the input list [1,null,2,2]
# root = TreeNode(1)            # Root node
# root.right = TreeNode(2)
# root.right.left = TreeNode(2)

# Manually constructing the BST from the input list [4, 3, 6, 2, null, 5, 6, 2, 3]
root = TreeNode(4)  # Root node
root.left = TreeNode(3)  # Left child of root
root.right = TreeNode(6)  # Right child of root

root.left.left = TreeNode(2)  # Left child of 3
root.right.left = TreeNode(5)  # Left child of 6
root.right.right = TreeNode(6)  # Right child of 6

root.left.left.left = TreeNode(2)  # Left child of 2
root.left.left.right = TreeNode(3)  # Right child of 2


def findMode(root):
    current_count = 0
    current_value = 0
    max_count = 0
    mode = []

    def inorder(node):
        nonlocal current_count, current_value, max_count, mode

        if node is None:
            return

        inorder(node.left)

        # check value
        if node.val == current_value:
            current_count += 1
        else:
            current_count = 1
            current_value = node.val

        # check count
        if current_count > max_count:
            max_count = current_count
            mode = [current_value]
        elif current_count == max_count:
            mode.append(current_value)

        inorder(node.right)

    inorder(root)
    return mode


print(findMode(root))

# Time complexity:
# O(h), where h is the height of the tree.
# In a balanced tree, this will be O(log n).
# In the worst case (a skewed tree), it will be O(n).

# Space complexity:
# O(h), due to the recursive call stack, which is proportional to the height of the tree.
