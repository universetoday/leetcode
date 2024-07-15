"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
------------------------
Дан числовой массив, поверни массив справа в точке k, так чтобы k последних элементов попали в начало массива.
------------------------
MEDIUM
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Изменяем k, если оно больше длины списка
        k = k % n
        # Функция переворачивания массива с позиции start до позиции end
        def reverse(nums, start, end):
            while start < end:
                # Меняем местами элементы
                nums[start], nums[end] = nums[end], nums[start]
                # Сдвигаем позицию start вправо
                start += 1
                # Сдвигаем позицию end влево
                end -= 1

        # Перевернем весь массив
        reverse(nums, 0, n - 1)
        # Перевернем обратно первые k элементов
        reverse(nums, 0, k - 1)
        # Перевернем оставшиеся элементы
        reverse(nums, k, n - 1)


nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
print(nums)

nums = [-1,-100,3,99]
k = 2
Solution().rotate(nums, k)
print(nums)
