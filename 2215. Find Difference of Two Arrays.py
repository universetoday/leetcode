"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.
------------------------
Учитывая два целочисленных массива nums1 и nums2 с индексом 0, верните список answer размера 2, где:

    answer[0] - это список всех различных целых чисел в nums1, которые отсутствуют в nums2.
    answer[1] - это список всех различных целых чисел в nums2, которые отсутствуют в nums1.

Обратите внимание, что целые числа в списках могут быть возвращены в любом порядке.
------------------------
EASY
"""
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1.difference(set2)), list(set2.difference(set1))]


"""
Для решения задачи требуется найти два списка:

    Первый список должен содержать все уникальные элементы из nums1, которые отсутствуют в nums2.
    Второй список должен содержать все уникальные элементы из nums2, которые отсутствуют в nums1.

Алгоритм решения:

    Преобразуем оба массива в множества (set), чтобы получить уникальные элементы и упростить операции сравнения.
    Используем операцию вычитания множеств для получения элементов, которые присутствуют в одном множестве, 
    но отсутствуют в другом.
    Вернем результат в виде списка, состоящего из двух списков.

    В этой функции сначала преобразуем nums1 и nums2 в множества, чтобы избавиться от дубликатов и упростить сравнение.
    Используем операцию вычитания множеств (set1 - set2), 
    чтобы найти элементы, которые есть в set1, но которых нет в set2. То же самое делаем для set2.
    Результаты сохраняем в два отдельных списка и возвращаем их в виде списка.

Таким образом, функция возвращает список из двух списков: первый содержит уникальные элементы из nums1, 
которые отсутствуют в nums2, а второй — уникальные элементы из nums2, которые отсутствуют в nums1.
"""

nums1 = [1,2,3]
nums2 = [2,4,6]
sol = Solution()
res = sol.findDifference(nums1, nums2)
print(res)
assert res == [[1,3],[4,6]]

nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
sol = Solution()
res = sol.findDifference(nums1, nums2)
print(res)
assert res == [[3],[]]
