"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
--------------------------------
Дан числовой массив, для каждого nums[i] найдите, сколько чисел в массиве меньше, чем оно.
Так, что для каждого nums[i] вы должны посчитать число, чтобы j != i и nums[j] < nums[i].
Возвратить массив с числами.
--------------------------------
EASY
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # отсортируем массив
        sorted_list = sorted(list(nums))
        print(sorted_list)
        length = len(nums)

        res_dict = {}
        # если число не в словаре, добавим его порядковый номер
        for i in range(length):
            if sorted_list[i] not in res_dict:
                res_dict[sorted_list[i]] = i

        # теперь создадим результирующий массив, куда запишем количества появлений чисел из массива nums
        # в нужном порядке
        res = []
        for i in range(length):
            res.append(res_dict[nums[i]])
        return res


nums = [8,1,2,2,3]
sol = Solution()
res = sol.smallerNumbersThanCurrent(nums)
print(res)
assert res == [4,0,1,1,3]

nums = [6,5,4,8]
sol = Solution()
res = sol.smallerNumbersThanCurrent(nums)
print(res)
assert res == [2,1,0,3]

nums = [7,7,7,7]
sol = Solution()
res = sol.smallerNumbersThanCurrent(nums)
print(res)
assert res == [0,0,0,0]
