"""You are given a string word containing lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters,
which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"],
we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters.
The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key.
You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below.
Note that 1, *, #, and 0 do not map to any letters.
---------------------------------------

---------------------------------------
EASY
"""
from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        # Подсчитать количество вхождений каждой буквы
        letter_count = Counter(word)

        # Отсортировать буквы по убыванию частоты
        sorted_letters = sorted(letter_count.items(), key=lambda item: -item[1])

        # Распределить буквы по клавишам
        presses = 0
        letter_index = 0  # Индекс буквы в сортированном списке

        # Рассчитываем нажатия для каждой клавиши (всего 8 клавиш: 2-9)
        for press_count in range(1, len(sorted_letters) // 8 + 2):
            for _ in range(8):
                if letter_index < len(sorted_letters):
                    letter, count = sorted_letters[letter_index]
                    presses += press_count * count
                    letter_index += 1

        return presses


word = "abcde"
sol = Solution()
res = sol.minimumPushes(word)
print(res)
assert res == 5

word = "xyzxyzxyzxyz"
sol = Solution()
res = sol.minimumPushes(word)
print(res)
assert res == 12

word = "aabbccddeeffgghhiiiiii"
sol = Solution()
res = sol.minimumPushes(word)
print(res)
assert res == 24
