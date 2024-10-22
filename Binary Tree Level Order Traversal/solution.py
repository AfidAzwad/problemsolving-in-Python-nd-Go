# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []

    q = deque([root])
    results = []

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        results.append(level)
    return results

# Manually constructing the BST from the input list [4, 2, 7, 1, 3]
root = TreeNode(3)            # Root node
root.left = TreeNode(9)        # Left child of root
root.right = TreeNode(20)       # Right child of root
root.right.left = TreeNode(15)   # Left child of node 2
root.right.right = TreeNode(7)  # Right child of node 2

print(levelOrder(root)) # [[3], [9, 20], [15, 7]]