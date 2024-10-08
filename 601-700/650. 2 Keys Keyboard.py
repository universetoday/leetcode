"""
There is only one character 'A' on the screen of a notepad.
You can perform one of two operations on this notepad for each step:

    Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.

Given an integer n, return the minimum number of operations
to get the character 'A' exactly n times on the screen.
-------------------------------
На экране текстового редактора есть только один символ 'A'.
Вы можете выполнять одно из двух операций на этом редакторе на каждом шаге:

1. Копировать все: вы можете скопировать все символы,
присутствующие на экране (частичное копирование не допускается).
2. Вставить: вы можете вставить символы, которые были скопированы в последний раз.

Заданное целое число n, верните минимальное количество операций,
чтобы получить символ 'A' ровно n раз на экране.
-------------------------------
MEDIUM
"""


class Solution:
    def minSteps(self, n: int) -> int:

        operations = 0
        i = 2
        while n > 1:
            while n % i == 0:
                operations += i
                n //= i
            i += 1
        return operations


"""
Чтобы решить эту задачу, нужно понять, что каждая операция "Копировать все" 
удваивает количество символов на экране, а операция "Вставить" добавляет количество символов, 
которое было скопировано ранее. Идея заключается в том, 
чтобы разбить число nn на множители и использовать эти множители, 
чтобы минимизировать количество операций.

Рассмотрим алгоритм:

    Разложение на множители: Для числа nn находим все его множители, начиная с наименьших.
    Использование множителей: Каждый множитель ii можно интерпретировать как:
        Сделать одну операцию "Копировать все", когда на экране имеется niin​ символов.
        Затем выполнить i−1i−1 операций "Вставить", чтобы получить i×ni=ni×in​=n символов.
    Минимизация операций: Продолжать этот процесс до тех пор, пока не достигнем числа nn.

Алгоритм можно описать следующим образом:

    Инициализируем переменную operations равную 0, которая будет подсчитывать количество операций.
    Начнем с числа i=2i=2 и будем пробегать все числа вплоть до nn. 
    Если nn делится на ii, то уменьшаем nn на ii, добавляя ii к operations.
    Повторяем процесс, пока nn не станет равным 1.

Пример работы алгоритма:

Если n=9n=9:

    Находим, что 9 = 3 * 3.
    Сначала нужно выполнить операцию "Копировать все", когда на экране 1 символ, 
    затем 2 раза вставить (получим 3 символа).
    Далее снова делаем операцию "Копировать все" и 2 раза вставляем (получаем 9 символов).
    Всего операций: 3 (Копировать все) + 2 (Вставить) + 3 (Копировать все) + 2 (Вставить) = 8 операций.

Таким образом, для числа n=9n=9 минимальное количество операций равно 6.
"""

n = 3
sol = Solution()
res = sol.minSteps(n)
print(res)
assert res == 3

n = 1
sol = Solution()
res = sol.minSteps(n)
print(res)
assert res == 0
