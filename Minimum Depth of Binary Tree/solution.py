# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually creating the binary tree [3, 9, 20, None, None, 15, 7]
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# The tree is now created as:
#       3
#      / \
#     9  20
#       /  \
#      15   7

# Manually creating the binary tree [2, null, 3, null, 4, null, 5, null, 6]
# root = TreeNode(2)
# root.right = TreeNode(3)
# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(5)
# root.right.right.right.right = TreeNode(6)

# The tree is now created as:
# 2
#  \
#   3
#    \
#     4
#      \
#       5
#        \
#         6

# Manually creating the binary tree [1, 2, 3, 4, null, null, 5]
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(5)

        #   1
        #  / \
        # 2   3
#        /     \
#       4       5


################################### Recursive DFS ###################################

def minDepthDFS(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    # If left subtree is None, consider only right subtree
    if root.left is None:
        return minDepthDFS(root.right) + 1

    # If right subtree is None, consider only left subtree
    if root.right is None:
        return minDepthDFS(root.left) + 1

    # If both left and right subtrees exist, take the minimum of both depths
    return min(minDepthDFS(root.left), minDepthDFS(root.right)) + 1

print('depth :',minDepthDFS(root))

# Time Complexity: O(n)
# Space Complexity: O(n)


################################### BFS ###################################

def minDepthBFS(root):
    if root is None:
        return 0

    level = 1
    q = deque([root])

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            val = node.val
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            if node.left is None and node.right is None:
                return level
        level += 1
    return level

print('depth :',minDepthBFS(root))

# Time Complexity: O(n)
# Space Complexity: O(h)

