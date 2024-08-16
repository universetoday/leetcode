"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times
as it shows in both arrays and you may return the result in any order.
------------------------------
Даны два целочисленных массива nums1 и nums2, нужно вывести массив их пересечения.
Каждый элемент в итоговом массива появляется столько раз, скоько он появляется в обоих массивах,
и вы возвращаете отсортированный результат.
------------------------------
EASY
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hash tables
        nums1_dict = {}
        nums2_dict = {}
        # Считаем сколько раз в списке nums1 встречается каждое число
        for i, num in enumerate(nums1):
            if num in nums1_dict:
                nums1_dict[num] += 1
            else:
                nums1_dict[num] = 1
        # Считаем сколько раз в списке nums2 встречается каждое число
        for i, num in enumerate(nums2):
            if num in nums2_dict:
                nums2_dict[num] += 1
            else:
                nums2_dict[num] = 1
        # Перебираем ключи словаря nums1_dict и добавляем в res ключи, встречающиеся в обоих словарях
        res = []
        for key in nums1_dict:
            value1 = nums1_dict[key]
            value2 = nums2_dict.get(key, 0)
            if value1 and value2:
                count = min(nums1_dict[key], nums2_dict[key])
                for i in range(count):
                    res.append(key)
        # выводим отсортированный список
        return sorted(res)


nums1 = [1,2,2,1]
nums2 = [2,2]
sol = Solution()
res = sol.intersect(nums1, nums2)
print(res)
assert res == [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
sol = Solution()
res = sol.intersect(nums1, nums2)
print(res)
assert res == [4,9]
