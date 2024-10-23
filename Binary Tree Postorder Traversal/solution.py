# Definition for a binary tree node.
from collections import deque
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually constructing the BST from the input list [1,2,3,4,5,null,8,null,null,6,7,9]
root = TreeNode(1)               # Level 1: Root node
root.left = TreeNode(2)          # Level 2: Left child of root
root.right = TreeNode(3)         # Level 2: Right child of root

root.left.left = TreeNode(4)     # Level 3: Left child of node 2
root.left.right = TreeNode(5)    # Level 3: Right child of node 2

root.right.right = TreeNode(8)   # Level 3: Right child of node 3
root.right.right.left = TreeNode(9)  # Level 4: Left child of node 8

root.left.right.left = TreeNode(6)   # Level 4: Left child of node 5
root.left.right.right = TreeNode(7)  # Level 4: Right child of node 5

def postorderTraversal(root):
    preOrderMap = []

    def postOrder(root):
        if not root:
            return
        postOrder(root.left)
        postOrder(root.right)
        preOrderMap.append(root.val)

    postOrder(root)
    return preOrderMap

print(postorderTraversal(root)) # [4,6,7,5,2,9,8,3,1]

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
