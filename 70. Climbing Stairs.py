"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
--------------------
Ты забираешься вверх по лестнице. Требуется n шагов, чтобы достичь вершины.

Каждый раз ты можешь подняться на одну или две ступени. Сколькими разными способами можно забраться наверх?
--------------------
EASY
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # Задача решается с использованием формулы по нахождению чисел Фибоначи
        if n <= 1:
            return 1

        prev = 1
        cur = 1
        for i in range(2, n + 1):
            next = prev + cur
            prev = cur
            cur = next
        return cur


n = 2
sol = Solution()
res = sol.climbStairs(n)
print(res)
assert res == 2

n = 3
sol = Solution()
res = sol.climbStairs(n)
print(res)
assert res == 3

n = 5
sol = Solution()
res = sol.climbStairs(n)
print(res)
assert res == 8
