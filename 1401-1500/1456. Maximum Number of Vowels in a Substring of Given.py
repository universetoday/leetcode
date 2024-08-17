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
        isVowel = lambda x: x in 'aeiou'
        sum_vowels = sum(map(isVowel, s[:k]))
        max_v = sum_vowels
        for i in range(len(s) - k):
            sum_vowels += isVowel(s[i+k]) - isVowel(s[i])
            max_v = max(max_v, sum_vowels)
        return max_v

"""
Объяснение:

    isVowel: Лямбда-функция, которая возвращает True, если символ является гласной.
    sum_vowels: Подсчет количества гласных в первом окне длиной k.
    max_v: Инициализируется текущим количеством гласных (sum_vowels), найденным в первом окне.
    Цикл: Перемещение окна с подсчетом гласных и обновлением max_v.
"""


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

s = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"
k = 33
sol = Solution()
res = sol.maxVowels(s, k)
print(res)
assert res == 7
