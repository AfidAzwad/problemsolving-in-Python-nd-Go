# Definition for a binary tree node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    left = head
    right = head

    # Move 'right' pointer ahead by 'n' steps
    while right and n > 0:
        right = right.next
        n -= 1

    if not right:
        return head.next

    # Move both 'left' and 'right' pointers until 'right' reaches the end
    while right.next:
        right = right.next
        left = left.next

    left.next = left.next.next

    return head

# Manually constructing the linked list from the list [1, 2, 3, 4, 5]
head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

n = 2
print(removeNthFromEnd(head,n))

# Edge cases :
# 1. if 1 Node and n=1
# 1. if 2 Node and n=2