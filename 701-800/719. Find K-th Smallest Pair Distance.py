"""
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k,
return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
------------------------
Есть массив целых чисел nums и целое число k.
Нужно найти k-ю наименьшую дистанцию среди всех возможных пар чисел в массиве nums.
------------------------
HARD
"""
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if self.count_pairs_with_distance_less_than_or_equal(nums, mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

    def count_pairs_with_distance_less_than_or_equal(self, nums, mid):
        count = 0
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] <= mid:
                j += 1
            count += j - i - 1
        return count

"""

"""

nums = [1,3,1]
k = 1
sol = Solution()
res = sol.smallestDistancePair(nums, k)
print(res)
assert res == 0

nums = [1,1,1]
k = 2
sol = Solution()
res = sol.smallestDistancePair(nums, k)
print(res)
assert res == 0

nums = [1,6,1]
k = 3
sol = Solution()
res = sol.smallestDistancePair(nums, k)
print(res)
assert res == 5

nums = [62,100,4]
k = 2
sol = Solution()
res = sol.smallestDistancePair(nums, k)
print(res)
assert res == 58
