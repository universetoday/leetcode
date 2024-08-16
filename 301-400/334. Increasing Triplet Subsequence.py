"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
---------------
Дан целочисленный массив nums, верните true, если существует тройка индексов (i, j, k), таких,
что i < j < k и nums[i] < nums[j] < nums[k]. Если такие индексы не существуют, верните false.
---------------
MEDIUM
"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False

"""
Мы инициализируем две переменные first и second значением бесконечности. 
Эти переменные будут хранить минимальные значения, которые мы встретим на пути, 
чтобы отслеживать потенциальные тройки.

Проходим по массиву. Для каждого элемента:

    Если текущий элемент меньше или равен first, обновляем first.
    Если текущий элемент больше first, но меньше или равен second, обновляем second.
    Если текущий элемент больше second, то мы нашли тройку, и можем вернуть True.

Если тройка не найдена в процессе прохода, возвращаем False."""

nums = [1,2,3,4,5]
sol = Solution()
res = sol.increasingTriplet(nums)
print(res)
assert res == True

nums = [5,4,3,2,1]
sol = Solution()
res = sol.increasingTriplet(nums)
print(res)
assert res == False

nums = [2,1,5,0,4,6]
sol = Solution()
res = sol.increasingTriplet(nums)
print(res)
assert res == True
