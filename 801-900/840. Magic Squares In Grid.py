"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column,
 and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
---------------
3 x 3 магический квадрат - это сетка 3 x 3, заполненная различными числами от 1 до 9 таким образом,
что каждая строка, столбец и обе диагонали имеют одинаковую сумму.

Учитывая сетку размером row x col, заполненную целыми числами, сколько 3 x 3 смежных магических квадратов
в ней содержится?

Примечание: хотя магический квадрат может содержать только числа от 1 до 9, сетка может содержать числа до 15.
---------------
MEDIUM
"""
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def check_magic(arr):
            # Преобразуем подматрицу в одномерный список
            nums = [num for row in subgrid for num in row]

            # Проверяем, что все числа уникальны и находятся в диапазоне от 1 до 9
            if set(nums) != set(range(1, 10)):
                return False

            # Список для хранения сумм
            res = []
            # Проверка горизонтальных и вертикальных линий
            for i in range(len(arr)):
                hor = arr[i][0] + arr[i][1] + arr[i][2]
                vert = arr[0][i] + arr[1][i] + arr[2][i]
                res.append(hor)
                res.append(vert)
            # Проверка диагоналей
            diag1 = arr[0][0] + arr[1][1] + arr[2][2]
            diag2 = arr[0][2] + arr[1][1] + arr[2][0]
            res.append(diag1)
            res.append(diag2)
            return all(x == 15 for x in res)

        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                subgrid = [row[j:j + 3] for row in grid[i:i + 3]]
                if check_magic(subgrid):
                    # print(check_magic(grid[i:i+3][j:j+3]))
                    count += 1
                    # print(count)
        return count


grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
sol = Solution()
res = sol.numMagicSquaresInside(grid)
print(res)
assert res == 1

grid = [[8]]
sol = Solution()
res = sol.numMagicSquaresInside(grid)
print(res)
assert res == 0
