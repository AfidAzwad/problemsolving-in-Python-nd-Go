class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create the linked list list1 : [1,2,4]
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Create the linked list list2 : [1,3,4]
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


def mergeTwoLists(list1, list2):
    dummy = ListNode()

    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1 and list2 is None:
        tail.next = list1
    elif list2 and list1 is None:
        tail.next = list2

    return dummy.next

print(mergeTwoLists(list1, list2))
