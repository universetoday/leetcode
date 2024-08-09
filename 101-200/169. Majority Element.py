"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
-------------------
Дан числовой массив размера n. Найди элемент, который появляется больше n/2 раз.
-------------------
EASY
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Создаем словарь для подсчета количества чисел
        result = {}
        max_element = 0
        max_count = 0
        for num in nums:
            # Если число не встречалось, то добавляем его в словарь со значением 1
            if num not in result:
                result[num] = 1
            # Иначе увеличиваем кол-во появлений числа на 1
            else:
                result[num] += 1
            # Если кол-во появлений числа больше максимально зафиксированного, то обновляем max_count
            # и max_element присваиваем это число
            if result[num] > max_count:
                max_count = result[num]
                max_element = num
        return max_element


nums = [3,2,3]
k = Solution().majorityElement(nums)
print(k)         # Вывод: 3

nums = [2,2,1,1,1,2,2]
k = Solution().majorityElement(nums)
print(k)         # Вывод: 2