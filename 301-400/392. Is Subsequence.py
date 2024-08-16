"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
---------------
Учитывая две строки s и t, верните true, если s является подпоследовательностью t, и false в противном случае.

Подпоследовательность строки - это новая строка, которая образована из исходной строки путем
удаления некоторых (может быть и ни одного) символов без нарушения относительных позиций оставшихся символов.
(т.е. "ace" является подпоследовательностью "abcde", в то время как "aec" - нет).
---------------
EASY
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        j = 0
        for i in range(len(t)):
            if s[j] == t[i]:
                j += 1
                if j == len(s):
                    return True
        return False


s = "abc"
t = "ahbgdc"
sol = Solution()
res = sol.isSubsequence(s, t)
print(res)
assert res == True

s = "axc"
t = "ahbgdc"
sol = Solution()
res = sol.isSubsequence(s, t)
print(res)
assert res == False

s = ""
t = "ahbgdc"
sol = Solution()
res = sol.isSubsequence(s, t)
print(res)
assert res == True

s = "b"
t = "abc"
sol = Solution()
res = sol.isSubsequence(s, t)
print(res)
assert res == True

s = "b"
t = "c"
sol = Solution()
res = sol.isSubsequence(s, t)
print(res)
assert res == False
