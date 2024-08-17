"""
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
------------------------

------------------------
MEDIUM
"""
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_ones = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_ones = max(max_ones, right - left + 1)

        return max_ones


"""
Чтобы решить задачу, нужно использовать метод "скользящего окна" (sliding window). 
Идея заключается в том, чтобы с помощью окна изменяемого размера проходить по массиву и 
подсчитывать количество единиц, при этом отслеживая максимальную длину подмассива, 
где можно изменить до k нулей на единицы.

Объяснение:

    left и right — это указатели, определяющие текущее окно в массиве nums.
    zero_count — это переменная, которая отслеживает количество нулей в текущем окне.
    Цикл for проходит по массиву с правой стороны, добавляя элементы в окно.
    Если количество нулей в окне превышает k, то левый указатель left сдвигается вправо, 
    уменьшая размер окна, пока количество нулей не станет допустимым.
    В каждой итерации проверяется максимальная длина окна, и результат сохраняется в max_ones.
"""

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
sol = Solution()
res = sol.longestOnes(nums, k)
print(res)
assert res == 6

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
sol = Solution()
res = sol.longestOnes(nums, k)
print(res)
assert res == 10
