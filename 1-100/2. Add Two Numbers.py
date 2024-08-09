"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Для решения этой задачи можно использовать следующий алгоритм:
        1. Пройти по каждому узлу обоих связанных списков, складывая соответствующие цифры
        2. Учитывать перенос на следующий разряд
        3. Создать новый связанный список для хранения результата
        """
        # Инициализируем dummy_head для представления узла результирующего списка
        dummy_head = ListNode(0)
        # Инициализируем указатель current для прохода по результирующему связанному списку
        current = dummy_head
        # Инициализируем carry для хранения переноса на следующий разряд
        carry = 0

        # Проходим по спискам l1 и l2, пока не достигнем конца обоих
        while l1 or l2 or carry:
            # Извлекаем значения текущих узлов
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            # Складываем значения x и y и перенос carry
            total = x + y + carry
            # Обновляем значение переноса
            carry = total // 10
            # Создаем новый узел с текущей цифрой
            current.next = ListNode(total % 10)
            # Переходим к следующему узлу в списках
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # Если после завершения цикла carry больше 0, то создаем еще один узел

        return dummy_head.next


l1_list = [2, 4, 3]
l1 = ListNode(l1_list[0], ListNode(l1_list[1], ListNode(l1_list[2])))
l2_list = [5, 6, 4]
l2 = ListNode(l2_list[0], ListNode(l2_list[1], ListNode(l2_list[2])))
sol = Solution()
res = sol.addTwoNumbers(l1, l2)
res_list = [7, 0, 8]
res_check = ListNode(res_list[0], ListNode(res_list[1], ListNode(res_list[2])))
while res_check:
    print(res_check.val, end=" ")
    res_check = res_check.next

print()

l1_list = [0]
l1 = ListNode(l1_list[0])
l2_list = [0]
l2 = ListNode(l2_list[0])
sol = Solution()
res = sol.addTwoNumbers(l1, l2)
res_list = [0]
res_check = ListNode(res_list[0])
while res_check:
    print(res_check.val, end=" ")
    res_check = res_check.next

print()

l1_list = [9, 9, 9, 9, 9, 9, 9]
l1 = ListNode(l1_list[0], ListNode(l1_list[1], ListNode(l1_list[2], ListNode(l1_list[3], ListNode(l1_list[4], ListNode(l1_list[5], ListNode(l1_list[6])))))))
l2_list = [9, 9, 9, 9]
l2 = ListNode(l2_list[0], ListNode(l2_list[1], ListNode(l2_list[2], ListNode(l2_list[3]))))
sol = Solution()
res = sol.addTwoNumbers(l1, l2)
res_list = [8, 9, 9, 9, 0, 0, 0, 1]
res_check = ListNode(res_list[0], ListNode(res_list[1], ListNode(res_list[2], ListNode(res_list[3], ListNode(res_list[4], ListNode(res_list[5], ListNode(res_list[6])))))))
while res_check:
    print(res_check.val, end=" ")
    res_check = res_check.next
