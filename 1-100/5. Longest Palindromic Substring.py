"""
Given a string s, return the longest
palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Если строка пустая, возвращаем пустую строку
        if not s:
            return ""
        # Инициализируем начальную позицию start и максимальную длину полиндрома max_length
        # и длину исходной строки length
        start = 0
        max_length = 1
        length = len(s)
        # Итерация с каждой позиции строки
        for i in range(1, length):
            # Указатели слева и справа от середины предполагаемого палиндрома
            # Проверяем две возможные длины палиндрома с центром в одной букве ('aba')
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and s[low] == s[high]:
                # Для каждой позиции мы расширяемся вправо и влево, пока символы совпадают
                # Если длина найденного палиндрома больше текущей максимальной длины,
                # то обновляем начальную позицию и длину палиндрома max_length
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                # сдвигаем указатели для следующей проверки
                low -= 1
                high += 1

            # Указатели слева и справа от середины предполагаемого палиндрома
            # Проверяем две возможные длины палиндрома с центром в двух одинаковых буквах ('abba')
            low = i - 1
            high = i
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1
        return s[start: start + max_length]



s = "babad"
sol = Solution()
res = sol.longestPalindrome(s)
print(res)
assert res == "bab"

s = "cbbd"
sol = Solution()
res = sol.longestPalindrome(s)
print(res)
assert res == "bb"
