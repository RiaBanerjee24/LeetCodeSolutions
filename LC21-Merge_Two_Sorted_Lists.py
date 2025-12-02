'''
Difficulty: Easy
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        while list1 and list2:
            if list1.val==list2.val:
                new_node = ListNode(list1.val)
                new_node2 = ListNode(list2.val)
                tail.next = new_node
                tail = tail.next
                tail.next = new_node2
                tail = tail.next
                list1 = list1.next
                list2 = list2.next
            elif list1.val<list2.val:
                new_node = ListNode(list1.val)
                tail.next = new_node
                tail = tail.next
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                tail.next = new_node
                tail = tail.next
                list2 = list2.next
        while list1 and not list2:
            new_node = ListNode(list1.val)
            tail.next = new_node
            tail = tail.next
            list1 = list1.next
        while list2 and not list1:
            new_node = ListNode(list2.val)
            tail.next = new_node
            tail = tail.next
            list2 = list2.next
        return dummy.next