"""
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '.
These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.
---------------
Сетка n x n состоит из квадратов 1 x 1, где каждый квадрат 1 x 1 состоит из символа '/', '\' или пробела ' '.
Эти символы разделяют квадрат на непрерывные области.

Учитывая сетку grid, представленную как массив строк, верните количество областей.

Обратите внимание, что символы обратной косой черты экранированы, поэтому '\' представлен как '\\'.
---
MEDIUM
"""
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = 3 * n
        graph = [[0] * size for _ in range(size)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    graph[3 * i][3 * j + 2] = 1
                    graph[3 * i + 1][3 * j + 1] = 1
                    graph[3 * i + 2][3 * j] = 1
                elif grid[i][j] == '\\':
                    graph[3 * i][3 * j] = 1
                    graph[3 * i + 1][3 * j + 1] = 1
                    graph[3 * i + 2][3 * j + 2] = 1

        def dfs(x, y):
            if x < 0 or x >= size or y < 0 or y >= size or graph[x][y] != 0:
                return
            graph[x][y] = 1
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        regions = 0
        for i in range(size):
            for j in range(size):
                if graph[i][j] == 0:
                    dfs(i, j)
                    regions += 1

        return regions


"""
Задача заключается в определении количества регионов в сетке размером n x n, состоящей из квадратов размером 1 x 1.
Каждый квадрат содержит либо символ '/', либо символ '', либо пробел ' '.
Эти символы делят квадрат на отдельные регионы.

Для того чтобы найти количество регионов, необходимо учитывать следующие факты:

    Символ '/' делит квадрат на две области, проходя по диагонали слева направо (сверху вниз).
    Символ '' делит квадрат на две области, проходя по диагонали справа налево (сверху вниз).
    Пробел не делит квадрат, так как это один регион.

Для решения задачи можно разбить каждый квадрат на 4 треугольника и использовать алгоритм объединения компонентов
(Union-Find) или поиск в глубину (DFS), чтобы подсчитать количество отдельных регионов.

Алгоритм решения:

    Разбейте каждый квадрат на 4 треугольника:
        Верхний левый треугольник (TL)
        Верхний правый треугольник (TR)
        Нижний левый треугольник (BL)
        Нижний правый треугольник (BR)
    Для символа /:
        TL и BR соединены.
        TR и BL соединены.
    Для символа \\:
        TL и TR соединены.
        BL и BR соединены.
    Для символа пробела:
        Все треугольники соединены.
    После разбиения примените DFS или Union-Find, чтобы подсчитать количество связанных компонент.
"""

grid = [" /","/ "]
sol = Solution()
res = sol.regionsBySlashes(grid)
print(res)
assert res == 2

grid = [" /","  "]
sol = Solution()
res = sol.regionsBySlashes(grid)
print(res)
assert res == 1

grid = ["/\\","\\/"]
sol = Solution()
res = sol.regionsBySlashes(grid)
print(res)
assert res == 5

grid = [" /","\\ "]
sol = Solution()
res = sol.regionsBySlashes(grid)
print(res)
assert res == 2
