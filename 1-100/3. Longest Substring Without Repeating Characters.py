"""
Given a string s, find the length of the longest
substring
without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. Пустой словарь char_index для хранения индексов символов,
        # longest - для хранения самой длинной подстроки и
        # start - для отслеживания начала текущей подстроки
        char_index = {}
        longest = 0
        start = 0

        # 2. Итерация: с помощью enumerate получаем индекс i и символ каждого элемента char
        for i, char in enumerate(s):
            # 3. Проверка на повторяющиеся символы:
            # если символ уже в словаре, обновить start
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            longest = max(longest, i - start + 1)

        return longest


s = "abcabcbb"
sol = Solution()
res = sol.lengthOfLongestSubstring(s)
print(res)
assert res == 3

s = "bbbbb"
sol = Solution()
res = sol.lengthOfLongestSubstring(s)
print(res)
assert res == 1

s = "pwwkew"
sol = Solution()
res = sol.lengthOfLongestSubstring(s)
print(res)
assert res == 3