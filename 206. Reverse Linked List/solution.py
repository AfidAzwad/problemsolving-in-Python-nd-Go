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


def reverseList(head):
    previous, current = None, head

    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    return previous

print(reverseList(head))

'''
    TC: O(n)
    SC: O(1)
'''