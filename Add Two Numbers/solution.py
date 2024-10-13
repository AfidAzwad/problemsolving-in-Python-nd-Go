# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2, ListNode(4, ListNode(3)))  # [2, 4, 3]
l2 = ListNode(5, ListNode(6, ListNode(4)))  # [5, 6, 4]

def addTwoNumbers(l1, l2):

    carry = 0
    newList = ListNode()
    current = newList

    while l1 or l2 or carry:  # Loop until both lists and the carry are exhausted
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10  # Carry for the next iteration
        current.next = ListNode(total % 10)  # Create the new node with the current sum
        current = current.next  # Move the pointer forward to the newly created node

        # Move to the next node in l1 and l2, if available
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return newList.next

newList = addTwoNumbers(l1,l2)


# Time Complexity: O(n)
# Space Complexity: O(n)
