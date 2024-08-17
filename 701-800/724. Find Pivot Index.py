"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly
to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array,
then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
------------------------

------------------------
EASY
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums) - nums[0]
        i = 0
        while left_sum != right_sum:
            if i == len(nums) - 1:
                return -1
            left_sum += nums[i]
            right_sum -= nums[i+1]
            i += 1

        return i if left_sum == right_sum else -1


"""
Задача заключается в нахождении "пивотного индекса" массива, такого, 
что сумма всех чисел слева от этого индекса равна сумме всех чисел справа от него. 
Если такой индекс существует, нужно вернуть его, если нет — вернуть -1.

Объяснение:

    Инициализация:
        Мы вычисляем total_sum — общую сумму всех элементов массива.
        left_sum изначально равна нулю, так как до первого элемента слева нет чисел.

    Итерация по массиву:
        Для каждого элемента на индексе i мы вычисляем right_sum, 
        как разницу между total_sum и суммой элементов слева плюс текущий элемент.
        Если в какой-то момент left_sum оказывается равной right_sum, 
        мы возвращаем текущий индекс i как пивотный индекс.

    Если ни один индекс не соответствует условию:
        Если ни один индекс не удовлетворяет условию задачи, возвращается -1.
"""

nums = [1,7,3,6,5,6]
sol = Solution()
res = sol.pivotIndex(nums)
print(res)
assert res == 3

nums = [1,2,3]
sol = Solution()
res = sol.pivotIndex(nums)
print(res)
assert res == -1

nums = [2,1,-1]
sol = Solution()
res = sol.pivotIndex(nums)
print(res)
assert res == 0


