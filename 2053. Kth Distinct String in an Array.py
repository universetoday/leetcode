"""A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
---------------------------------------

---------------------------------------
EASY
"""
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash_table = {}
        position = {}
        for i, letter in enumerate(arr):
            if letter not in hash_table:
                hash_table[letter] = 1
                position[letter] = i
            else:
                hash_table[letter] += 1
        res_dict = {}
        for letter in hash_table:
            if hash_table[letter] == 1:
                res_dict[position[letter]] = letter
        keys = sorted(list(res_dict.keys()))
        if k > len(keys):
            return ''
        return res_dict[keys[k-1]]


arr = ["d","b","c","b","c","a"]
k = 2
sol = Solution()
res = sol.kthDistinct(arr, k)
print(res)
assert res == "a"

arr = ["aaa","aa","a"]
k = 1
sol = Solution()
res = sol.kthDistinct(arr, k)
print(res)
assert res == "aaa"

arr = ["a","b","a"]
k = 3
sol = Solution()
res = sol.kthDistinct(arr, k)
print(res)
assert res == ""
