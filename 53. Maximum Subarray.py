"""
Given an integer array nums, find the
subarray
with the largest sum, and return its sum.
"""


class Solution(object):
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Для решения этой задачи можно использовать алгоритм Кадане (Kadane's Algorithm).
        """
        # 1. Устанавливаем max_current и max_global равными первому элементу массива nums
        max_current = nums[0]
        max_global = nums[0]

        # 2. Итерация: Проходим по оставшимся элементам массива
        for num in nums[1:]:
            # 3. Для каждого элемента вычисляем max_current как максимум
            # между текущим числом num и текущей суммой max_current
            max_current = max(num, num + max_current)
            # 4. Обновляем max_global, если max_current больше max_global
            if max_current > max_global:
                max_global = max_current

        return max_global


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
res = sol.maxSubArray(nums)
print(res)
assert res == 6

nums = [1]
sol = Solution()
res = sol.maxSubArray(nums)
print(res)
assert res == 1

nums = [5, 4, -1, 7, 8]
sol = Solution()
res = sol.maxSubArray(nums)
print(res)
assert res == 23
