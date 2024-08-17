"""There are n kids with candies. You are given an integer array candies,
where each candies[i] represents the number of candies the ith kid has,
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if,
after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
---------------------------------------

---------------------------------------
EASY
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        res = []
        for candy in candies:
            if candy + extraCandies >= maximum:
                res.append(True)
            else:
                res.append(False)
        return res


candies = [2,3,5,1,3]
extraCandies = 3
sol = Solution()
res = sol.kidsWithCandies(candies, extraCandies)
print(res)
assert res == [True,True,True,False,True]

candies = [4,2,1,1,2]
extraCandies = 1
sol = Solution()
res = sol.kidsWithCandies(candies, extraCandies)
print(res)
assert res == [True,False,False,False,False]

candies = [12,1,12]
extraCandies = 10
sol = Solution()
res = sol.kidsWithCandies(candies, extraCandies)
print(res)
assert res == [True,False,True]
