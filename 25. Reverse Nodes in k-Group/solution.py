class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create the linked list: [1,2,3,4,5]
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Link the nodes together
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head
    prevGroup = dummy

    def get_kth_node(prevGroup, k):
        """
        Helper function to get the kth node from the given node.
        If there are fewer than k nodes remaining, return None.

        Parameters:
        prevGroup (ListNode): The previous group's tail.
        k (int): The number of nodes to traverse.

        Returns:
        ListNode or None: The kth node if it exists, else None.
        """
        for _ in range(k):
            prevGroup =  prevGroup.next
        return prevGroup

    while True:
        # Get the kth node from the current position
        kth = get_kth_node(prevGroup, k)
        if not kth:  # If fewer than k nodes remain, stop processing
            break

        nextGroup = kth.next  # Pointer to the node after the kth node

        # Reverse k nodes between prevGroup.next and kth
        prev, current = kth.next, prevGroup.next
        while current != nextGroup:
            temp = current.next  # Store next node
            current.next = prev  # Reverse the pointer
            prev = current  # Move prev forward
            current = temp  # Move current forward

        # Update the previous group's next pointer
        temp = prevGroup.next  # Store the start of the reversed group
        prevGroup.next = kth  # Connect previous group with the kth node
        prevGroup = temp  # Move prevGroup to the end of the newly reversed group

    return dummy.next  # Return the new head of the reversed list

k = 3
new_head = reverseKGroup(head, k)

# Print the modified linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

"""
Time Complexity: O(n)
- Each node is visited at most twice (once for counting, once for reversing).
- Reversing k nodes takes O(k) time, and we do this for approximately n/k groups.
- So overall, O(n) time complexity.

Space Complexity: O(1)
- We use only a few extra pointers for tracking nodes.
- No additional data structures are used, so the space complexity is constant.
"""
