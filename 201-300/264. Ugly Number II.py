"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.
------------------------
«Некрасивое число» — это положительное целое число,
простые множители которого ограничены числами 2, 3 и 5.

Заданное целое число n, верните n-е некрасивое число.
------------------------
MEDIUM
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1

        i2 = i3 = i5 = 0
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        for i in range(1, n):
            next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            ugly[i] = next_ugly

            if next_ugly == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2

            if next_ugly == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3

            if next_ugly == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5

        return ugly[-1]

"""
Чтобы найти nn-й уродливый номер (Ugly Number), 
можно использовать метод динамического программирования с тремя указателями. 
Этот метод эффективен и позволяет находить требуемый результат за линейное время.

Вот алгоритм:

    Создайте массив ugly, который будет содержать первые nn уродливых чисел.
    Инициализируйте три указателя: i2, i3, i5, которые будут указывать на последний индекс, 
    умноженный на 2, 3 и 5 соответственно.
    Инициализируйте первые значения для каждого множителя:
        next_multiple_of_2 = 2 * ugly[i2]
        next_multiple_of_3 = 3 * ugly[i3]
        next_multiple_of_5 = 5 * ugly[i5]
    В каждом шаге выберите минимальное значение из трех next_multiple_of и добавьте его в массив ugly.
    Обновите соответствующий указатель и пересчитайте следующее значение для этого указателя.

Временная сложность:

    Временная сложность этого подхода составляет O(n)O(n). 
    Это связано с тем, что мы генерируем ровно nn уродливых чисел, 
    и для каждого из них выполняется фиксированное количество операций 
    (сравнение и обновление указателей). Следовательно, 
    общая временная сложность линейно зависит от nn.

Пространственная сложность:

    Пространственная сложность этого подхода составляет O(n)O(n). 
    Это связано с тем, что мы используем массив ugly размером nn 
    для хранения первых nn уродливых чисел. Помимо этого массива, 
    используется лишь постоянное количество дополнительной памяти для указателей 
    (i2, i3, i5) и переменных для хранения следующих множителей 
    (next_multiple_of_2, next_multiple_of_3, next_multiple_of_5). 
    Таким образом, общая пространственная сложность составляет O(n)O(n).
"""

n = 10
sol = Solution()
res = sol.nthUglyNumber(n)
print(res)
assert res == 12

n = 1
sol = Solution()
res = sol.nthUglyNumber(n)
print(res)
assert res == 1
