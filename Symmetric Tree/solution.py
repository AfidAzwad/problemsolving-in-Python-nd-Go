# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    def sameTree(p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return sameTree(p.left, q.right) and sameTree(p.right, q.left)
        return False

    if sameTree(root.left, root.right):
        return True

    return False

# Manually constructing the binary tree from the input list [1, 2, 2, 3, 4, 4, 3]
root = TreeNode(1)                    # Root node
root.left = TreeNode(2)               # Left child of root
root.right = TreeNode(2)              # Right child of root
root.left.left = TreeNode(3)          # Left child of node 2 (left)
root.left.right = TreeNode(4)         # Right child of node 2 (left)
root.right.left = TreeNode(4)         # Left child of node 2 (right)
root.right.right = TreeNode(3)        # Right child of node 2 (right)


print(isSymmetric(root))