# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    current = root

    if current is None:
        return TreeNode(val)

    if val < current.val:
        current.left = insertIntoBST(current.left, val)
    else:
        current.right = insertIntoBST(current.right, val)

    return current

# Manually constructing the BST from the input list [4, 2, 7, 1, 3]
root = TreeNode(4)            # Root node
root.left = TreeNode(2)        # Left child of root
root.right = TreeNode(7)       # Right child of root
root.left.left = TreeNode(1)   # Left child of node 2
root.left.right = TreeNode(3)  # Right child of node 2

val = 5
print(insertIntoBST(root,val))

# Time complexity:
# O(h), where h is the height of the tree.
# In a balanced tree, this will be O(log n).
# In the worst case (a skewed tree), it will be O(n).

# Space complexity:
# O(h), due to the recursive call stack, which is proportional to the height of the tree.