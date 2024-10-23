# Definition for a binary tree node.
from collections import deque
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually constructing the BST from the input list [5, 3, 6, 2, 4, None, None, 1]
root = TreeNode(5)             # Root node
root.left = TreeNode(3)        # Left child of root
root.right = TreeNode(6)       # Right child of root
root.left.left = TreeNode(2)   # Left child of node 3
root.left.right = TreeNode(4)  # Right child of node 3
root.left.left.left = TreeNode(1)  # Left child of node 2

def kthSmallest(root,k):
    q = deque([root])
    max_heap = [] # size at most k

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            heapq.heappush(max_heap, -node.val)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
    return -max_heap[0]

k=3
print(kthSmallest(root,k))

# Approach : BFS with MinHeap
# as min heap maintain the smallest value in root when we pop a value it will remove the smallest value.
# Here ultimate head size will be k and that means kth element is in the index 0.