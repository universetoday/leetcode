"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
-------------------------------

-------------------------------
EASY
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Helper function to check if s1 is divisible by s2
        def is_divisible(s1, s2):
            if len(s1) % len(s2) != 0:
                return False
            return s1 == s2 * (len(s1) // len(s2))

        # Helper function to find gcd of two strings
        def gcd(s1, s2):
            while s2:
                s1, s2 = s2, s1[:len(s1) % len(s2)]
            return s1

        # Check if the two strings can be divided by the same substring
        if not is_divisible(str1 + str2, str2 + str1):
            return ""

        return gcd(str1, str2)


word1 = "ABCABC"
word2 = "ABC"
sol = Solution()
res = sol.gcdOfStrings(word1, word2)
print(res)
assert res == "ABC"

word1 = "ABABAB"
word2 = "ABAB"
sol = Solution()
res = sol.gcdOfStrings(word1, word2)
print(res)
assert res == "AB"

word1 = "LEET"
word2 = "CODE"
sol = Solution()
res = sol.gcdOfStrings(word1, word2)
print(res)
assert res == ""

word1 = "ABABABAB"
word2 = "ABAB"
sol = Solution()
res = sol.gcdOfStrings(word1, word2)
print(res)
assert res == "ABAB"
