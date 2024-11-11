# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree nodes based on the structure above [5,4,8,11,null,13,4,7,2,null,null,null,1]
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)

root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == targetSum

    # Recursively check the left and right subtrees
    targetSum -= root.val
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)

targetSum = 5

print(hasPathSum(root, targetSum))