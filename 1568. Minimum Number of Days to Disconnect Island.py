"""
You are given an m x n binary grid grid where 1 represents land and 0 represents water.
An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.
---------------
Вам дана двоичная сетка grid размера m x n, где 1 представляет землю, а 0 представляет воду.
Остров - это максимальная группа 1-ок, связанная в 4 направлениях (горизонтально или вертикально).

Считается, что сетка связана, если у нас ровно один остров, в противном случае она считается несвязанной.

В один день нам разрешается изменить любую одну ячейку земли (1) в ячейку воды (0).

Верните минимальное количество дней, необходимое для отсоединения сетки.
---------------
HARD
"""
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def is_connected():
            def dfs(x, y):
                if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] or grid[x][y] == 0:
                    return
                visited[x][y] = True
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dfs(x + dx, y + dy)

            visited = [[False] * n for _ in range(m)]
            island_count = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        island_count += 1
                        if island_count > 1:
                            return False
                        dfs(i, j)
            return island_count == 1

        def can_disconnect_in_one_day():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                        if not is_connected():
                            grid[i][j] = 1
                            return True
                        grid[i][j] = 1
            return False

        m, n = len(grid), len(grid[0])

        # Шаг 1: Проверяем, если уже несвязанная сетка
        if not is_connected():
            return 0

        # Шаг 2: Проверяем, можно ли разъединить сетку за 1 день
        if can_disconnect_in_one_day():
            return 1

        # Шаг 3: Если нельзя за 1 день, то всегда можно за 2 дня
        return 2


"""
Задача заключается в определении минимального количества дней, необходимых для того, 
чтобы сделать сетку (grid) "несвязанной". 
Сетка представляет собой бинарную матрицу размером m x n, где 1 обозначает сушу, а 0 обозначает воду. 
Остров определяется как максимальная группа соединенных по горизонтали или вертикали клеток, содержащих 1.

Сетка считается связанной, если в ней есть ровно один остров. 
Если после удаления одной клетки с сушей, 
сетка становится несвязанной, задача считается решенной.
Алгоритм решения:

    Проверка на начальную несвязанность:
        Если изначально сетка уже несвязана (имеет более одного острова), то ответ будет 0 (никакие дни не нужны).

    Проверка возможности разъединения за один день:
        Пройти по всем клеткам с сушей (1). Для каждой клетки:
            Превратить её временно в воду (0).
            Проверить, не стала ли сетка несвязанной после этого.
            Если да, вернуть 1 как минимальное количество дней.
            Восстановить клетку обратно в сушу.

    Проверка возможности разъединения за два дня:
        Если нельзя разъединить сетку за один день, то всегда можно разъединить сетку за два дня, 
        так как любой остров можно разделить, удалив две соседние клетки с сушей.
"""


grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
sol = Solution()
res = sol.minDays(grid)
print(res)
assert res == 2

grid = [[1,1]]
sol = Solution()
res = sol.minDays(grid)
print(res)
assert res == 2
