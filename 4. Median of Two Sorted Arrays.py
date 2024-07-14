"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
------------------------------------------------------
Задача: даны два отсортированных массива nums1 и nums2 размером m и n соответственно.
Необходимо найти медиану объединенного отсортированного массива,
при этом общая сложность по времени выполнения должна быть O(log(m+n)).
------------------------------------------------------
HARD
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # # Убедимся, что nums1 является меньшим из двух массивов
        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1
        # m = len(nums1)
        # n = len(nums2)
        # imin = 0
        # imax = m
        # half_len = (m + n + 1) // 2
        # # Используем бинарный поиск, чтобы найти правильное разделение объединенного массива
        # while imin <= imax:
        #     # Переменные i и j представляют индексы, где разделяются nums1 и nums2 соответственно
        #     i = (imin + imax) // 2
        #     j = half_len - i
        #     # Мы находим i так, чтобы все элементы слева от i и j были меньше или равны всем элементам справа
        #     if i < m and nums1[i] < nums2[j - 1]:
        #         imin = i + 1
        #     elif i > 0 and nums1[i - 1] > nums2[j]:
        #         imax = i - 1
        #     else:
        #         # Как только мы найдем правильное разделение, медиана будет либо максимумом левой половины,
        #         # если общее количество элементов нечетное,
        #         # либо средним значением максимума левой и минимума правой половины,
        #         # если количество четное
        #         if i == 0: max_of_left = nums2[j - 1]
        #         elif j == 0: max_of_left = nums1[i - 1]
        #         else: max_of_left = max(nums1[i - 1], nums2[j - 1])
        #
        #         # Если длина массива нечетная, то медианой будет срединный элемент
        #         if (m + n) % 2 == 1:
        #             return max_of_left / 1.0
        #
        #         if i == m: min_of_right = nums2[j]
        #         elif j == n: min_of_right = nums1[i]
        #         else: min_of_right = max(nums1[i], nums2[j])
        #
        #         # Если длина массива четная, то медианой будет средней двух занчений в середине массива
        #         return (max_of_left + min_of_right) / 2.0
        #

        res_list = sorted(nums1 + nums2)
        length = len(res_list)
        median_index = length // 2
        if length % 2 == 1:
            return res_list[median_index] / 1
        else:
            left = res_list[median_index - 1]
            right = res_list[median_index]
            return (left + right) / 2
        # O(N*logN)



nums1 = [1, 3]
nums2 = [2]
sol = Solution()
res = sol.findMedianSortedArrays(nums1, nums2)
print(res)
assert res == 2.0

nums1 = [1, 2]
nums2 = [3, 4]
sol = Solution()
res = sol.findMedianSortedArrays(nums1, nums2)
print(res)
assert res == 2.5

nums1 = [1, 3]
nums2 = [2, 7]
sol = Solution()
res = sol.findMedianSortedArrays(nums1, nums2)
print(res)
assert res == 2.5