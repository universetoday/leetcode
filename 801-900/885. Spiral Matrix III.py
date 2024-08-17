"""You start at the cell (rStart, cStart) of an rows x cols grid facing east.
The northwest corner is at the first row and column in the grid,
and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid.
Whenever you move outside the grid's boundary,
we continue our walk outside the grid (but may return to the grid boundary later.).
Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.
---------------------------------------
Вы начинаете в ячейке (rStart, cStart) сетки размером rows x cols, смотрите на восток.
Северо-западный угол находится в первом ряду и столбце сетки,
а юго-восточный угол - в последнем ряду и столбце.

Вы будете ходить по часовой спирали, чтобы посетить каждую позицию в этой сетке.
Каждый раз, когда вы выходите за границы сетки,
мы продолжаем наше движение за пределами сетки (но можем вернуться к границе сетки позже).
В конечном итоге, мы посещаем все rows * cols ячеек сетки.

Верните массив координат, представляющих позиции сетки в порядке их посещения.
---------------------------------------
MEDIUM
"""
from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i, j = rStart, cStart

        diri, dirj = 0, 1  # directions to move
        twice = 2
        res = []
        moves = 1
        next_moves = 2

        while len(res) < (rows * cols):
            if (-1 < i < rows) and (-1 < j < cols):
                res.append([i, j])

            i += diri
            j += dirj
            moves -= 1
            if moves == 0:
                diri, dirj = dirj, -diri  # 90 deg Clockwise
                twice -= 1
                if twice == 0:
                    twice = 2
                    moves = next_moves
                    next_moves += 1
                else:
                    moves = next_moves - 1
        return res



"""
Чтобы обойти сетку размером rows x cols по спирали, начиная с точки (rStart, cStart) и двигаясь по часовой стрелке, 
нам нужно следовать определенному алгоритму. Давайте опишем этот алгоритм по шагам:

    Инициализация:
        Задаем начальные координаты (rStart, cStart).
        Определяем начальное направление (направо - восток).

    Обход по спирали:
        Создаем массив для хранения координат посещенных ячеек.
        Используем массив для направления (восток, юг, запад, север).
        Сохраняем границы (верхнюю, нижнюю, левую и правую) и корректируем их при каждом изменении направления.
        Перемещаемся по сетке, добавляя координаты в массив и проверяя, не пересекли ли мы границы.

    Смена направления:
        При достижении границы сетки или уже посещенной ячейки, изменяем направление (восток -> юг -> запад -> север).

Алгоритм будет продолжаться до тех пор, пока не будут посещены все ячейки сетки.
"""
rows = 1
cols = 4
rStart = 0
cStart = 0
sol = Solution()
res = sol.spiralMatrixIII(rows, cols, rStart, cStart)
print(res)
assert res == [[0,0],[0,1],[0,2],[0,3]]

rows = 5
cols = 6
rStart = 1
cStart = 4
sol = Solution()
res = sol.spiralMatrixIII(rows, cols, rStart, cStart)
print(res)
assert res == [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
