class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually constructing the BST from the input list [1,2,3,null,5]
root = TreeNode(1)             # Root node
root.left = TreeNode(2)        # Left child of root
root.right = TreeNode(3)       # Right child of root
root.left.right = TreeNode(5) # Right child of node 3


def binaryTreePaths(root):
    if not root:
        return []

    result = []

    def dfs(node, path):
        if not node:
            return

        # If it's not the first node, add '->'
        if path:
            path += '->' + str(node.val)
        else:
            path = str(node.val)

        if not node.left and not node.right:
            result.append(path)
        else:
            dfs(node.left, path)
            dfs(node.right, path)

    # Start DFS with the root node
    dfs(root, "")
    return result


print(binaryTreePaths(root))