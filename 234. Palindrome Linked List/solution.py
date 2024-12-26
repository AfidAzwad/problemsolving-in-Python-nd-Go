class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create the linked list: [1, 2, 2, 1]
node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(2)
node1.next.next.next = ListNode(1)

# Now node1 is the head of the linked list with a cycle
head = node1


def isPalindrome(head):
    if not head or not head.next:
        return True

    # find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the linked list
    previous, current = None, slow

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    # compare with first half
    current = head

    while previous:
        if previous.val != current.val:
            return False
        previous = previous.next
        current = current.next
    return True

print(isPalindrome(head))


# Time Complexity : O(n)(first while loop)+O(n)(second while loop) = O(n)

# Why It’s Not 𝑂(𝑛2):
# Key Point: These loops are sequential, not nested. The second while loop runs after the first loop has finished.
# Since they run one after the other, their time complexities are added rather than multiplied.


# Space Complexity: O(1) — The algorithm uses only a constant amount of extra space