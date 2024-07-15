"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
---------------
Дан массив из чисел, передвинь все нули в конец массива, сохраняя порядок оставшихся чисел.

Заметь, что ты должен сделать это на месте без копирования массива
---------------
EASY
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Указатель на последний найденный ноль
        last_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_zero], nums[i] = nums[i], nums[last_zero]
                last_zero += 1


nums = [0,1,0,3,12]
sol = Solution()
sol.moveZeroes(nums)
print(nums)
assert nums == [1,3,12,0,0]

nums = [0]
sol = Solution()
sol.moveZeroes(nums)
print(nums)
assert nums == [0]


