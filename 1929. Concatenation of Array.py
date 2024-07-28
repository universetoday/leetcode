"""
Given an integer array nums of length n,
you want to create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
---------------------------
Дан целочисленный массив длиной n, вам нужно создвть массив длиной 2n,
где ans[i] == nums[i] и ans[i + n] == nums[i]
---------------------------
EASY
"""
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


nums = [1,2,1]
sol = Solution()
res = sol.getConcatenation(nums)
print(res)
assert res == [1,2,1,1,2,1]


nums = [1,3,2,1]
sol = Solution()
res = sol.getConcatenation(nums)
print(res)
assert res == [1,3,2,1,1,3,2,1]
