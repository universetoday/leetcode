"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
--------------
Задача: дан целочисленный массив nums, отсортированный в порядке возрастания (со значениями, не имеющими повторений),
который возможно был повернут вокруг неизвестного индекса k (1 <= k < nums.length).
Например, массив [0,1,2,4,5,6,7] мог быть повернут вокруг индекса 3 и стать [4,5,6,7,0,1,2].

Дан массив nums после возможного поворота и целое число target.
Необходимо вернуть индекс target, если он присутствует в nums, или -1, если его там нет.

Алгоритм должен иметь временную сложность O(log n).
--------------
MEDIUM
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
sol = Solution()
res = sol.search(nums, target)
print(res)
assert res == 4

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
sol = Solution()
res = sol.search(nums, target)
print(res)
assert res == -1

nums = [1]
target = 0
sol = Solution()
res = sol.search(nums, target)
print(res)
assert res == -1

