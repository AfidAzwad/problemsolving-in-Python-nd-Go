class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create the linked list: [1,1,2,3,3,4,5]
head = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)
node6 = ListNode(4)
node7 = ListNode(5)

# Link the nodes together
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7


def deleteDuplicates(head):
    # Create a dummy node to handle edge cases (e.g., when head itself needs to be removed)
    dummy = ListNode(0)
    dummy.next = head
    current = dummy  # Pointer to build the resulting linked list

    # Traverse the linked list
    while head:
        # If current node has a duplicate
        if head.next and head.val == head.next.val:
            # Skip all nodes with the same value
            while head.next and head.val == head.next.val:
                head = head.next
            # Point current's next to the node after the duplicates
            current.next = head.next
        else:
            # Move the `current` pointer forward if no duplicates
            current = current.next
        head = head.next

    return dummy.next

print(deleteDuplicates(head))

'''
    TC: O(n)
    - Each node in the linked list is visited exactly once.
    - The inner while loop skips duplicate nodes, but overall, every node is processed once.
    - Total time complexity: O(n), where n is the number of nodes in the linked list.

    SC: O(1)
    - The algorithm uses a constant amount of extra space (dummy node and a few pointers).
    - No additional data structures are created.
    - Total space complexity: O(1).
'''