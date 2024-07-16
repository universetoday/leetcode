"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
-----------------------------
Дан отсортированный массив неубывающих целых чисел, возврати индекс, если цель найдена.
Если нет, возврати индекс, где она бы находилась, если бы присутствовала в ряду.

Ты должен написать алгоритм с O(log n) временной сложностью.
-----------------------------
EASY
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Используем бинарный поиск с двумя указателями
        left = 0
        right = len(nums)
        if left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left # + 1 : иногда бывает ошибка по непонятной причине


nums = [1,3,5,6]
target = 5
res = Solution().searchInsert(nums, target)
print(res)
assert res == 2

nums = [1,3,5,6]
target = 2
res = Solution().searchInsert(nums, target)
print(res)
assert res == 1

nums = [1,3,5,6]
target = 7
res = Solution().searchInsert(nums, target)
print(res)
assert res == 4

