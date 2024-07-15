"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
---------------------
Дан числовой массив, содержащий n + 1
---------------------
MEDIUM
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Используем алгоритм Флойда для детектирования цикла, инициализируем черепаху и зайца
        tortoise = nums[0]
        hare = nums[0]

        # Находим точку пересечения циклов черепахи и зайца
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        # Черепаху возвращаем в начало
        tortoise = nums[0]
        # Находим повторяющийся элемент
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare


nums = [1,3,4,2,2]
res = Solution().findDuplicate(nums)
print(res)
assert res == 2


nums = [3,1,3,4,2]
res = Solution().findDuplicate(nums)
print(res)
assert res == 3

nums = [3,3,3,3,3]
res = Solution().findDuplicate(nums)
print(res)
assert res == 3
