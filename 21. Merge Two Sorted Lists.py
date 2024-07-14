"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
--------------------
Даны два начала двух отсортированных связанных списков list1 и list2.

Соедините два списка в один отсортированный список.
Возвратите начало объединенного связанного списка.
--------------------
EASY
"""

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res_list = ListNode()
        tail = res_list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1 or list2:
            tail.next = list1 if list1 else list2
        return res_list.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
sol = Solution()
res = sol.mergeTwoLists(list1, list2)
res_check = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
while res_check:
    print(res_check.val, end=" ")
    res_check = res_check.next

print()

list1 = ListNode()
list2 = ListNode()
sol = Solution()
res = sol.mergeTwoLists(list1, list2)
res_check = ListNode()
while res_check:
    print(res_check.val, end=" ")
    res_check = res_check.next

print()

list1 = ListNode()
list2 = ListNode(0)
sol = Solution()
res = sol.mergeTwoLists(list1, list2)
res_check = ListNode(0)
while res_check:
    print(res_check.val, end=" ")
    res_check = res_check.next