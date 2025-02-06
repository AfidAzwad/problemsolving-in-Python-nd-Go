# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually constructing the tree from the input list [1,2,2,3,3,null,null,4,4]
# root = TreeNode(1)                     # Level 1: Root node
#
# root.left = TreeNode(2)                # Level 2: Left child of root
# root.right = TreeNode(2)               # Level 2: Right child of root
#
# root.left.left = TreeNode(3)           # Level 3: Left child of the first 2
# root.left.right = TreeNode(3)          # Level 3: Right child of the first 2
#
# root.left.left.left = TreeNode(4)      # Level 4: Left child of the first 3
# root.left.right.right = TreeNode(4)    # Level 4: Right child of the second 3

# Manually constructing the tree from the input list [1, 2, 2, 3, null, null, 3, 4, null, null, 4]
root = TreeNode(1)                   # Level 1: Root node

root.left = TreeNode(2)              # Level 2: Left child of root
root.right = TreeNode(2)             # Level 2: Right child of root

root.left.left = TreeNode(3)         # Level 3: Left child of the first 2
root.right.right = TreeNode(3)       # Level 3: Right child of the second 2

root.left.left.left = TreeNode(4)    # Level 4: Left child of the first 3
root.right.right.right = TreeNode(4) # Level 4: Right child of the second 3

def isBalanced(root):
    def dfs(root):
        if root is None:
            return 0, True

        left_height, left_balanced = dfs(root.left)
        right_height, right_balanced = dfs(root.right)

        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return max(left_height, right_height) + 1, balanced

    _, result = dfs(root)
    return result


print(isBalanced(root))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
