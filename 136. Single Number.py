"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
-----------------
Дан непустой массив из чисел, каждый элемент которого появляется дважды за исключением одного.
Найди этот элемент.

Ты должен применить решение с линейной сложностью и использовать только постоянное дополнительное пространство.
-----------------
EASY
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if num not in result:
                result[num] = 1
            else:
                result.pop(num)
        return list(result.keys())[0]


nums = [2,2,1]
sol = Solution()
res = sol.singleNumber(nums)
print(res)
assert res == 1

nums = [4,1,2,1,2]
sol = Solution()
res = sol.singleNumber(nums)
print(res)
assert res == 4

nums = [1]
sol = Solution()
res = sol.singleNumber(nums)
print(res)
assert res == 1

