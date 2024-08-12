"""
Given a string s and an integer k,
return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
------------------------

------------------------
MEDIUM
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        isWovel = lambda x: x in 'aeiou'
        sum_vowels = sum(map(isWovel, s[:k]))
        max_v = 0
        for i in range(len(s) - k):
            substr = s[i:i+k]
            sum_vowels += isWovel(s[i+k]) - isWovel(s[i])
            max_v = max(max_v, sum_vowels)
        return max_v


s = "abciiidef"
k = 3
sol = Solution()
res = sol.maxVowels(s, k)
print(res)
assert res == 3

s = "aeiou"
k = 2
sol = Solution()
res = sol.maxVowels(s, k)
print(res)
assert res == 2

s = "leetcode"
k = 3
sol = Solution()
res = sol.maxVowels(s, k)
print(res)
assert res == 2

