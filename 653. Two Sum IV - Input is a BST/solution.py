class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually constructing the BST from [5, 3, 6, 2, 4, null, 7]
root = TreeNode(2)               # Level 1: Root node
root.left = TreeNode(1)          # Level 2: Left child of root
root.right = TreeNode(3)         # Level 2: Right child of root

root.left.left = TreeNode(2)     # Level 3: Left child of node 3
root.left.right = TreeNode(4)    # Level 3: Right child of node 3
root.right.right = TreeNode(7)   # Level 3: Right child of node 6


def findTarget(root, k):
    arr = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        arr.append(node.val)
        inorder(node.right)

    # to get sorted array
    inorder(root)

    L, R = 0, len(arr)-1

    while L < R:
        total = arr[L] + arr[R]
        if total == k:
            return True
        elif total > k:
            R -= 1
        else:
            L += 1
    return False

k = 9
print(findTarget(root, k)) # [5,3,6,2,4,null,7]

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
