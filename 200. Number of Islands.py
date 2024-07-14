"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
------------------------
Задача: дан двумерный бинарный массив grid размером m x n,
который представляет карту, где '1' означает сушу, а '0' — воду.
Необходимо вернуть количество островов.

Остров окружен водой и образован соединением прилегающих земель горизонтально или вертикально.
 Вы можете предположить, что все четыре края сетки окружены водой.
------------------------
Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
------------------------
MEDIUM
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        pass


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
sol = Solution()
res = sol.numIslands(grid)
print(res)
assert res == 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
sol = Solution()
res = sol.numIslands(grid)
print(res)
assert res == 3


