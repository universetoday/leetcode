"""
Two strings are considered close if you can attain one from the other using the following operations:

    Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character,
    and do the same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
------------------------
Две строки считаются близкими, если вы можете получить одну из другой, используя следующие операции:

    Операция 1: Поменять местами любые два существующих символа.
        Например, abcde -> aecdb
    Операция 2: Преобразовать каждое вхождение одного существующего символа в другой существующий символ,
    и сделать то же самое с другим символом.
        Например, aacabb -> bbcbaa (все a превращаются в b, а все b превращаются в a)

Вы можете использовать эти операции на любой строке столько раз, сколько необходимо.

Учитывая две строки, word1 и word2, вернуть true, если word1 и word2 близки, и false в противном случае.
------------------------
MEDIUM
"""
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Сравнение множеств символов
        if set(word1) != set(word2):
            return False

        # Сравнение частот символов
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())


"""
Задача требует определить, можно ли преобразовать одну строку в другую с помощью двух типов операций:

    Swap (Перестановка): Можно поменять местами любые два символа в строке.
    Transform (Трансформация): Можно заменить все вхождения одного символа на другой и наоборот.

Чтобы две строки можно было считать "близкими", они должны удовлетворять нескольким условиям:
Основные условия:

    Одинаковое множество символов: Оба слова должны содержать одинаковые символы. 
    Например, если одно слово содержит символ 'a', а другое нет, они не могут быть преобразованы друг в друга.

    Одинаковые частоты символов: Частоты всех символов должны совпадать. 
    Например, если в одном слове символ 'a' встречается 3 раза, а в другом 2 раза, 
    их нельзя преобразовать друг в друга.
"""

word1 = "abc"
word2 = "bca"
sol = Solution()
res = sol.closeStrings(word1, word2)
print(res)
assert res == True

word1 = "a"
word2 = "aa"
sol = Solution()
res = sol.closeStrings(word1, word2)
print(res)
assert res == False

word1 = "cabbba"
word2 = "abbccc"
sol = Solution()
res = sol.closeStrings(word1, word2)
print(res)
assert res == True
