# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually constructing the BST from the input list [5,1,4,null,null,3,6]
root = TreeNode(2)            # Root node
root.left = TreeNode(1)        # Left child of root
root.right = TreeNode(3)       # Right child of root

root.right.left = TreeNode(3)   # Left child of node 2
root.right.right = TreeNode(6)  # Right child of node 2

def isValidBST(root):
    def dfs(root, left, right):
        if not root:
            return True
        if not (left < root.val < right):
            return False
        return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
    return dfs(root, float('-inf'), float('inf'))

print(isValidBST(root))