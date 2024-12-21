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

def rotateRight(head, k):
    if not head:
        return head

    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length
    if k == 0:
        return head

    current = head
    for i in range(length - k - 1): # '-1' because we are starting from node 1
        current = current.next

    newHead = current.next
    current.next = None
    tail.next = head

    print(newHead)

    return newHead


k = 2

print(rotateRight(head, k))


# Time Complexity : O(n)(first while loop)+O(n)(second while loop) = O(n)

# Why It’s Not 𝑂(𝑛2):
# Key Point: These loops are sequential, not nested. The second while loop runs after the first loop has finished.
# Since they run one after the other, their time complexities are added rather than multiplied.


# Space Complexity: O(1) — The algorithm uses only a constant amount of extra space