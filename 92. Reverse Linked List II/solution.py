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


def reverseBetween(head, left, right):
    # Step 1: Create a dummy node to simplify edge cases (like reversing from head)
    dummy = ListNode(0)
    dummy.next = head
    leftPrevious, current = dummy, head

    # Step 2: Move leftPrevious and current to the starting point of reversal
    for _ in range(left - 1):
        leftPrevious, current = current, current.next  # Move both pointers forward

    # Step 3: Reverse the sublist from 'left' to 'right'
    previous = None
    for _ in range(right - left + 1):
        temp = current.next
        current.next = previous
        previous = current
        current = temp

    # Step 4: Reconnect the reversed portion with the original list
    leftPrevious.next.next = current  # Connect the last node of reversed sublist to next part
    leftPrevious.next = previous  # Connect the previous node to the reversed head

    return dummy.next  # Return new head (in case the head was reversed)


# Utility function to print linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Reverse the sublist between left and right
left = 2
right = 4
reversed_head = reverseBetween(head, left, right)

# Print the modified list
printList(reversed_head)

'''
    Time Complexity: O(n)
    - The function traverses the list twice:
      1. Once to reach the 'left' position (O(left)).
      2. Another pass to reverse the sublist (O(right - left)).
    - Since these add up to at most O(n), the overall complexity is O(n).

    Space Complexity: O(1)
    - The algorithm modifies the list in place using a few pointers.
    - No extra data structures are used, so space complexity remains O(1).
'''

