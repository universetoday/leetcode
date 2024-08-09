"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
-------------------------------
Даны две строки - needle и haystack, найди индекс первого вхождения needle в haystack.
-------------------------------
EASY
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)
        for i in range(n - m + 1):
            if haystack[i: i+m] == needle:
                return i
        return -1


haystack = "sadbutsad"
needle = "sad"
sol = Solution()
res = sol.strStr(haystack, needle)
print(res)
assert res == 0

haystack = "leetcode"
needle = "leeto"
sol = Solution()
res = sol.strStr(haystack, needle)
print(res)
assert res == -1
