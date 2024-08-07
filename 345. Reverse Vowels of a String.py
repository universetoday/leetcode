"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
---------------------------------------

---------------------------------------
EASY
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        left = 0
        right = len(s) - 1
        vowels = 'aeiouAEIOU'
        while left < right:
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
            if s[left] in vowels and s[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s[left]
                left += 1
                right -= 1
        return ''.join(s_list)


s = "hello"
sol = Solution()
res = sol.reverseVowels(s)
print(res)
assert res == "holle"

s = "leetcode"
sol = Solution()
res = sol.reverseVowels(s)
print(res)
assert res == "leotcede"


