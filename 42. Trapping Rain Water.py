"""
Given n non-negative integers representing an elevation map
where the width of each bar is 1,
compute how much water it can trap after raining.
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Для решения этой задачи можно использовать алгоритм Кадане (Kadane's Algorithm).
        """

        pass


height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
res = sol.trap(height)
print(res)
assert res == 6

height = [4,2,0,3,2,5]
sol = Solution()
res = sol.trap(height)
print(res)
assert res == 9
