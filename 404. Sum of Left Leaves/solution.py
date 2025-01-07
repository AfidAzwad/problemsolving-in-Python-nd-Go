class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root):
    total = 0

    def inorder(node):
        nonlocal total
        if node is None:
            return

        # Check if the left node is a leaf node
        if node.left and node.left.left is None and node.left.right is None:
            total += node.left.val

        inorder(node.left)
        inorder(node.right)

    inorder(root)
    return total


# Example tree: [3, 9, 20, null, null, 15, 7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Find and print the sum of left leaves
print(sumOfLeftLeaves(root))  # Output: 24 (9 + 15)

# Time complexity: O(n)
# - We visit every node once during the inorder traversal. n is the number of nodes in the tree.
# Space complexity: O(h)
# - The space complexity is O(h) due to the recursion stack, where h is the height of the tree.
# - In the worst case (a skewed tree), this would be O(n). For a balanced tree, this would be O(log n).
