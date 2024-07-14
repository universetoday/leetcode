"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
----------------
Дано начало односвязного списка, переверните список и возвратите его.
----------------
EASY
"""

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Изначально предыдущий узел отсутствует
        prev = None
        # Текущий узел начинается с головы списка
        current = head
        while current:
            # Временная переменная для хранения следующего узла
            next = current.next
            # Меняем направление ссылки текущего узла
            current.next = prev
            # Перемещаем предыдущий узел на текущий
            prev = current
            # Перемещаем текущий узел на следующий
            current = next
        return prev


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
res = sol.reverseList(head )
res_check = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
while res_check:
    print(res_check.val, end=" ")
    res_check = res_check.next

print()

head = ListNode(1, ListNode(2))
sol = Solution()
res = sol.reverseList(head )
res_check =  ListNode(2, ListNode(1))
while res_check:
    print(res_check.val, end=" ")
    res_check = res_check.next
