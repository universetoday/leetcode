"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude
between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
------------------------

------------------------
EASY
"""
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = altitude = 0
        for key in gain:
            altitude += key
            if altitude > max_altitude:
                max_altitude = altitude
        return max_altitude

"""
Задача заключается в том, чтобы найти самую высокую точку на пути байкера, 
исходя из данных о приросте высоты между соседними точками.
Пояснение задачи:

    Байкер начинает свое путешествие с точки 0 на высоте 0.
    Вам дан массив gain, где каждый элемент gain[i] представляет собой изменение высоты между точками i и i + 1.
    Необходимо найти максимальную высоту, которую достигнет байкер в ходе своего путешествия.

Пример:

Предположим, что gain = [-5, 1, 5, 0, -7].

    Байкер начинает на высоте 0.
    На первом этапе он спускается на 5 единиц: 0+(−5)=−50+(−5)=−5.
    Затем он поднимается на 1 единицу: −5+1=−4−5+1=−4.
    Потом он поднимается еще на 5 единиц: −4+5=1−4+5=1.
    Затем высота остается неизменной: 1+0=11+0=1.
    Наконец, он спускается на 7 единиц: 1−7=−61−7=−6.

Самая высокая точка за весь путь — это 1.
Алгоритм решения:

    Инициализируем текущую высоту current_altitude равной 0 и максимальную высоту max_altitude равной 0.
    Проходим по каждому элементу массива gain:
        Обновляем текущую высоту: прибавляем к ней значение gain[i].
        Если текущая высота больше максимальной, обновляем max_altitude.
    После завершения прохода возвращаем max_altitude как результат.

Пояснение кода:

    В начале высота равна 0.
    Мы проходим по массиву gain и на каждом шаге обновляем текущую высоту.
    Если текущая высота превышает предыдущую максимальную высоту, то обновляем значение максимальной высоты.
    В конце возвращаем максимальную высоту, достигнутую в ходе пути.

Таким образом, функция вычисляет и возвращает наивысшую точку, достигнутую байкером в ходе его поездки.
"""

gain = [-5,1,5,0,-7]
sol = Solution()
res = sol.largestAltitude(gain)
print(res)
assert res == 1

gain = [-4,-3,-2,-1,4,3,2]
sol = Solution()
res = sol.largestAltitude(gain)
print(res)
assert res == 0
