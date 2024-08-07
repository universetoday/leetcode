"""You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.
---------------------------------------
У вас есть поднос с горшками, на котором некоторые горшки заняты, а некоторые нет.
Тем не менее цветы немогут быть посажены в соседних горшках.

Учитывая, что массив состоит из 0 и 1, где 0 значит пустой, а 1 значит непустой, и число n,
верните True, если n новых цветов может быть посажено на этом подносе без нарушения правила соседних горшков,
и False в обратном случае.
---------------------------------------
HARD
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n



flowerbed = [1,0,0,0,1]
n = 1
sol = Solution()
res = sol.canPlaceFlowers(flowerbed, n)
print(res)
assert res == True

flowerbed = [1,0,0,0,1]
n = 2
sol = Solution()
res = sol.canPlaceFlowers(flowerbed, n)
print(res)
assert res == False

flowerbed = [1,0,0,0,1,0,0,1]
n = 2
sol = Solution()
res = sol.canPlaceFlowers(flowerbed, n)
print(res)
assert res == False

flowerbed = [1,0,0,0,1,0,0,0,1]
n = 2
sol = Solution()
res = sol.canPlaceFlowers(flowerbed, n)
print(res)
assert res == True

