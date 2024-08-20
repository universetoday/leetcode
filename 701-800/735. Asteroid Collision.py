"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right,
negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.
-------------------------------
Нам дан массив asteroids, представляющий астероиды в ряду.

Для каждого астероида абсолютное значение представляет его размер,
а знак означает его направление (положительное — это движение вправо,
отрицательное — влево). Каждый астероид движется с одинаковой скоростью.

Найдите состояние астероидов после всех столкновений.
Если два астероида встречаются, меньший будет уничтожен.
Если оба астероида одинакового размера, оба будут уничтожены.
Два астероида, движущиеся в одном направлении, никогда не встретятся.
-------------------------------
MEDIUM
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack


"""
Для решения задачи столкновения астероидов можно использовать стек (stack). Стек позволяет нам удобно обрабатывать столкновения астероидов, учитывая их направления и размеры.
Пошаговое решение:

    Мы будем проходить по каждому астероиду в массиве.
    Если стек пуст или текущий астероид движется вправо (положительное число), мы добавляем его в стек.
    Если текущий астероид движется влево (отрицательное число):
        Мы проверяем верхний элемент стека.
        Если верхний элемент стека — астероид, который движется вправо, то возможен конфликт:
            Если по абсолютному значению текущий астероид больше, то астероид из стека взрывается, и мы продолжаем сравнивать текущий астероид с новым верхним элементом стека.
            Если оба астероида одинакового размера, оба взрываются, и мы переходим к следующему астероиду.
            Если астероид в стеке больше по абсолютному значению, то текущий астероид взрывается, и мы не добавляем его в стек.
        Если стек пуст или на вершине стека астероид, движущийся влево, мы добавляем текущий астероид в стек.
    После обработки всех астероидов в стеке останутся те, которые выжили.
"""


asteroids = [5,10,-5]
sol = Solution()
res = sol.asteroidCollision(asteroids)
print(res)
assert res == [5,10]

asteroids = [8,-8]
sol = Solution()
res = sol.asteroidCollision(asteroids)
print(res)
assert res == []

asteroids = [10,2,-5]
sol = Solution()
res = sol.asteroidCollision(asteroids)
print(res)
assert res == [10]
