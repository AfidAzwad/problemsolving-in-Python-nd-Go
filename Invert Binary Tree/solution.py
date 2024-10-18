# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually constructing the BST from the input list [4,2,7,1,3,6,9]
root = TreeNode(4)            # Root node
root.left = TreeNode(2)        # Left child of root
root.right = TreeNode(7)       # Right child of root

root.left.left = TreeNode(1)   # Left child of node 2
root.left.right = TreeNode(3)  # Right child of node 2

root.right.left = TreeNode(6)  # Left child of node 7
root.right.right = TreeNode(9) # Right child of node 7

def invertTree(root):
    current = root

    if current is None:
        return current

    if current.left or current.right:
        current.left, current.right = current.right, current.left

    if current.left:
        invertTree(current.left)

    if current.right:
        invertTree(current.right)

    return current

print(invertTree(root))