"""
Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.
------------------------------

------------------------------
EASY
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # Count the number of zeros in the array
        zeros_count = arr.count(0)
        n = len(arr)

        # Start from the end of the array
        for i in range(n - 1, -1, -1):
            # Check if current index + number of zeros encountered is within bounds
            if i + zeros_count < n:
                arr[i + zeros_count] = arr[i]

            # If the current element is zero, we need to duplicate it
            if arr[i] == 0:
                zeros_count -= 1
                if i + zeros_count < n:
                    arr[i + zeros_count] = 0


arr = [1,0,2,3,0,4,5,0]
sol = Solution()
sol.duplicateZeros(arr)
print(arr)
assert arr == [1,0,0,2,3,0,0,4]

arr = [1,2,3]
sol = Solution()
sol.duplicateZeros(arr)
print(arr)
assert arr == [1,2,3]


