"""Given an integer array nums,
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
---------------------------------------

---------------------------------------
MEDIUM
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Step 1: Calculate prefix products and store in result
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Step 2: Calculate suffix products and multiply directly in result
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

"""  
Explanation:

    Step 1 (Prefix products):
        We initialize prefix to 1.
        We iterate over the array, and for each element at index i, we set result[i] to the product of all the elements to the left of nums[i] using the prefix variable.
        After setting result[i], we update prefix by multiplying it with nums[i].

    Step 2 (Suffix products):
        We initialize suffix to 1.
        We iterate over the array from right to left, and for each element at index i, we multiply result[i] by the product of all the elements to the right of nums[i] using the suffix variable.
        After updating result[i], we update suffix by multiplying it with nums[i].

This approach ensures that we only use O(1) extra space (excluding the output array) and achieve the desired O(n) time complexity.
"""

nums = [1,2,3,4]
sol = Solution()
res = sol.productExceptSelf(nums)
print(res)
assert res == [24,12,8,6]

nums = [-1,1,0,-3,3]
sol = Solution()
res = sol.productExceptSelf(nums)
print(res)
assert res == [0,0,9,0,0]
