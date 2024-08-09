"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence.
----------------------------
Дан целочисленный массив, возврати длину самой длинной возрастающей последовательности.
----------------------------
MEDIUM
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        result = [nums[0]]
        for i in range(length):
            num = nums[i]

            if num > result[-1]:
                result.append(num)
            else:
                left = 0
                right = length - 1
                while left < right:
                    mid = (left + right) // 2
                    if result[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                result[left] = num
        return len(result)


nums = [10,9,2,5,3,7,101,18]
res = Solution().lengthOfLIS(nums)
print(res)
assert res == 4

nums = [0,1,0,3,2,3]
res = Solution().lengthOfLIS(nums)
print(res)
assert res == 4

nums = [7,7,7,7,7,7,7]
res = Solution().lengthOfLIS(nums)
print(res)
assert res == 1

