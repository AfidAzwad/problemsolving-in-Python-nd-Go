class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create the linked list: [4,1,8,4,5]
node1 = ListNode(4)
node2 = ListNode(1)
node3 = ListNode(8)
node4 = ListNode(4)
node5 = ListNode(5)

# Link the nodes together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Now node1 is the head of the linked list with a cycle
headA = node1


# Create the linked list: [5,6,1,8,4,5]
node1 = ListNode(5)
node2 = ListNode(6)
node3 = ListNode(1)
node4 = ListNode(8)
node5 = ListNode(4)
node6 = ListNode(5)

# Link the nodes together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# Now node1 is the head of the linked list with a cycle
headB = node1

def getIntersectionNode(self, headA, headB):
    pointerA, pointerB = headA, headB

    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA
    return pointerA


print(getIntersectionNode(headA,headB))

# Time Complexity: O(n+m)
# Space Complexity: O(1)
