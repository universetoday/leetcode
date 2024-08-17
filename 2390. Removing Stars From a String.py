"""
You are given a string s, which contains stars *.

In one operation, you can:

    Choose a star in s.
    Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note:

    The input will be generated such that the operation is always possible.
    It can be shown that the resulting string will always be unique.
------------------------
Вам дана строка s, которая содержит символы звезды *.

В одной операции вы можете:

1. Выбрать звезду в s.
2. Удалить ближайший не-звездный символ слева от нее, а также удалить саму звезду.

Верните строку после удаления всех звезд.

Примечание:

- Входные данные будут генерироваться так, чтобы операция всегда была возможна.
- Можно показать, что результирующая строка всегда будет уникальной.
------------------------
MEDIUM
"""
from collections import Counter


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isalpha():
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)


"""
Этот код решает задачу, в которой требуется обработать строку s, 
содержащую буквы и символы, где символы определяют, как нужно модифицировать строку. 
Решение можно описать следующим образом:

    Инициализация стека:
        Создается пустой список stack, который будет использоваться как стек для хранения букв.

    Итерация по символам строки s:
        Для каждого символа c в строке:
            Если c является буквой (определяется с помощью c.isalpha()), 
            она добавляется в стек с помощью stack.append(c).
            Если c не является буквой 
            (предположительно, это символ, указывающий на удаление предыдущей буквы), 
            то последняя добавленная в стек буква удаляется с помощью stack.pop().

    Формирование итоговой строки:
        После того, как весь входной массив был обработан, 
        все оставшиеся в стеке буквы объединяются в одну строку с помощью "".join(stack).
        Эта строка является итоговым результатом работы алгоритма.

Пример работы:

Предположим, что строка s выглядит так: "ab#c".

    Шаг 1: Инициализация пустого стека: stack = [].
    Шаг 2: Проходим по строке:
        c = 'a': так как это буква, добавляем её в стек: stack = ['a'].
        c = 'b': это тоже буква, добавляем её в стек: stack = ['a', 'b'].
        c = '#': это не буква, поэтому удаляем последний элемент из стека: stack = ['a'].
        c = 'c': это буква, добавляем её в стек: stack = ['a', 'c'].
    Шаг 3: Соединяем элементы стека в строку: результат — "ac".

Итог:

Этот алгоритм эффективно обрабатывает строку с операциями добавления и удаления букв, 
используя стек. В конце он возвращает окончательную строку, 
которая была построена с учётом всех удалений.
"""

s = "leet**cod*e"
sol = Solution()
res = sol.removeStars(s)
print(res)
assert res == "lecoe"

s = "erase*****"
sol = Solution()
res = sol.removeStars(s)
print(res)
assert res == ""
