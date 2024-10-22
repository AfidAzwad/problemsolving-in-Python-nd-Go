# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root, subRoot):
    if not root:
        return False
    if not subRoot:
        return True

    def sameTree(r, s):
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            return sameTree(r.left, s.left) and sameTree(r.right, s.right)
        return False

    if sameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

# Correct root creation (based on [3,4,5,1,2,null,null,null,null,0]):
root = TreeNode(3)                   # Root node is 3
# root.left = TreeNode(4)              # Left child of root (3) is 4
# root.right = TreeNode(5)             # Right child of root (3) is 5
# root.left.left = TreeNode(1)         # Left child of node 4 is 1
# root.left.right = TreeNode(2)        # Right child of node 4 is 2
# root.left.right.left = TreeNode(0)   # Left child of node 2 is 0

# Correct subRoot creation (based on [4,1,2]):
subRoot = TreeNode(3)                # Root of subRoot is 4
# subRoot.left = TreeNode(1)           # Left child of subRoot (4) is 1
# subRoot.right = TreeNode(2)          # Right child of subRoot (4) is 2

print(isSubtree(root,subRoot))