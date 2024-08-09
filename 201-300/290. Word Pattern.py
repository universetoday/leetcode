"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match,
such that there is a bijection between a letter in pattern and a non-empty word in s.
-------------------------------
Даны две строки - pattern и s, узнайте, следует ли строка этому паттерну.
Здесь следует означает полное совпадение так,
что присутствует биекция между буквой в pattern и словом в строке s.
-------------------------------
EASY
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        res_dict = {}
        res_dict_invert = {}
        for i, key in enumerate(s_list):
            res_dict[pattern[i]] = s_list[i]

        for i, key in enumerate(s_list):
            res_dict_invert[s_list[i]] = pattern[i]

        for i, key in enumerate(s_list):
            if res_dict[pattern[i]] != s_list[i]:
                return False
            if res_dict_invert[s_list[i]] != pattern[i]:
                return False

        return True


pattern = "abba"
s = "dog cat cat dog"
sol = Solution()
res = sol.wordPattern(pattern, s)
print(res)
assert res == True

pattern = "abba"
s = "dog cat cat fish"
sol = Solution()
res = sol.wordPattern(pattern, s)
print(res)
assert res == False

pattern = "aaaa"
s = "dog cat cat dog"
sol = Solution()
res = sol.wordPattern(pattern, s)
print(res)
assert res == False

pattern = "abba"
s = "dog dog dog dog"
sol = Solution()
res = sol.wordPattern(pattern, s)
print(res)
assert res == False

pattern = "aba"
s = "cat cat cat do"
sol = Solution()
res = sol.wordPattern(pattern, s)
print(res)
assert res == False
