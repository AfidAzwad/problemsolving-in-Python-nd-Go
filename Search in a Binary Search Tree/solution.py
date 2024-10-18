# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    current = root

    while current:
        if current.val == val:
            return current
        if current.val > val:
            current = current.left
        else:
            current = current.right

    return None

# Manually constructing the BST from the input list [4, 2, 7, 1, 3]
root = TreeNode(4)            # Root node
root.left = TreeNode(2)        # Left child of root
root.right = TreeNode(7)       # Right child of root
root.left.left = TreeNode(1)   # Left child of node 2
root.left.right = TreeNode(3)  # Right child of node 2

val = 2
print(searchBST(root,val))