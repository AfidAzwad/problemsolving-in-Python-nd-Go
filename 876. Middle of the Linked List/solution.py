class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create the linked list: [1, 2, 2, 1]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

def middleNode(head):
    if not head:
        return head

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

print(middleNode(head))


# Time Complexity: O(n)
# Space Complexity: O(1)