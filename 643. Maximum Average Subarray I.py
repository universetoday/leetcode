"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.
---------------

---------------
EASY
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Вычисляем сумму первых k элементов
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # Используем скользящее окно для вычисления сумм остальных подмассивов длины k
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)

        # Возвращаем максимальное среднее значение
        return max_sum / k


nums = [1,12,-5,-6,50,3]
k = 4
sol = Solution()
res = sol.findMaxAverage(nums, k)
print(res)
assert res == 12.75

nums = [5]
k = 1
sol = Solution()
res = sol.findMaxAverage(nums, k)
print(res)
assert res == 5
