"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
-------------------------------

-------------------------------
EASY
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for a, b in zip(word1, word2):
            res.append(a + b)
        res.append(word1[len(word2):])
        res.append(word2[len(word1):])

        return "".join(res)


word1 = "abc"
word2 = "pqr"
sol = Solution()
res = sol.mergeAlternately(word1, word2)
print(res)
assert res == "apbqcr"

word1 = "ab"
word2 = "pqrs"
sol = Solution()
res = sol.mergeAlternately(word1, word2)
print(res)
assert res == "apbqrs"

word1 = "abcd"
word2 = "pq"
sol = Solution()
res = sol.mergeAlternately(word1, word2)
print(res)
assert res == "apbqcd"
