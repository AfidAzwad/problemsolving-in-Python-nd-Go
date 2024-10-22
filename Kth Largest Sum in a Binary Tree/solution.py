# Definition for a binary tree node.
from collections import deque
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually constructing the BST from the input list [5,8,9,2,1,3,7,4,6]
root = TreeNode(5)             # Level 1: Root node

root.left = TreeNode(8)        # Level 2: Left child of root
root.right = TreeNode(9)       # Level 2: Right child of root

root.left.left = TreeNode(2)   # Level 3: Left child of node 8
root.left.right = TreeNode(1)  # Level 3: Right child of node 8
root.right.left = TreeNode(3)  # Level 3: Left child of node 9
root.right.right = TreeNode(7) # Level 3: Right child of node 9

root.left.left.left = TreeNode(4)  # Level 4: Left child of node 2
root.left.left.right = TreeNode(6) # Level 4: Right child of node 2

def kthLargestLevelSum(root,k):
    q = deque([root])
    min_heap = [] # size at most k

    while q:
        level_sum = 0
        for _ in range(len(q)):
            node = q.popleft()
            level_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        heapq.heappush(min_heap, level_sum)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0] if len(min_heap) == k else -1

k=2
print(kthLargestLevelSum(root,k))

# Approach : BFS with MinHeap
# as min heap maintain the smallest value in root when we pop a value it will remove the smallest value.
# Here ultimate head size will be k and that means kth element is in the index 0.