class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create the linked list: [3, 2, 1, 4]
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(4)

# Link the nodes together
node1.next = node2
node2.next = node3
node3.next = node4

# Now node1 is the head of the linked list with a cycle
head = node1

def insertionSortList(head):
    dummy = ListNode(0)
    dummy.next = head
    prev, current = head, head.next

    while current:
        if current.val > prev.val:
            prev, current = current, current.next
            continue

        temp = dummy

        while current.val > temp.next.val:
            temp = temp.next

        prev.next = current.next
        current.next = temp.next
        temp.next = current
        current = prev.next
    return dummy.next

print(insertionSortList(head))


# Time Complexity : O(n)(first while loop)+O(n)(second while loop) = O(n)

# Why It’s Not 𝑂(𝑛2):
# Key Point: These loops are sequential, not nested. The second while loop runs after the first loop has finished.
# Since they run one after the other, their time complexities are added rather than multiplied.


# Space Complexity: O(1) — The algorithm uses only a constant amount of extra space