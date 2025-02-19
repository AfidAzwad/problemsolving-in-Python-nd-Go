class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    root = TreeNode(postorder[-1])
    mid = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:mid], postorder[:mid])
    root.right = buildTree(inorder[mid+1:], postorder[mid:-1])
    return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

print(buildTree(inorder, postorder))

# Time complexity: O(n), where n is the number of nodes in the tree.
# Space complexity: O(h), where h is the height of the tree, due to the recursion stack.
