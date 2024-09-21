.. _intersection-of-2-linked-lists:

=============================
160. Intersection of Two Linked Lists
=============================

**Problem Statement**

    Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

**Example 1:**

.. code-block::
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.

    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.
