class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create the linked list: [3, 2, 0, -4]
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Link the nodes together
node1.next = node2
node2.next = node3
node3.next = node4

# Create a cycle: -4 points back to node2 (which has value 2)
node4.next = node2

# Now node1 is the head of the linked list with a cycle
head = node1

def detectCycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            index = 0
            while slow != fast:
                slow = slow.next
                fast = fast.next
                index += 1
            return 'tail connects to node index %s' % index
    return 'There is no cycle in the linked list.'
print(detectCycle(head))


# Time Complexity : O(n)(first while loop)+O(n)(second while loop) = O(n)

# Why It’s Not 𝑂(𝑛2):
# Key Point: These loops are sequential, not nested. The second while loop runs after the first loop has finished.
# Since they run one after the other, their time complexities are added rather than multiplied.


# Space Complexity: O(1) — The algorithm uses only a constant amount of extra space