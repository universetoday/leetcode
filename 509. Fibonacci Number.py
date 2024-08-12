"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
------------------------

------------------------
EASY
"""


class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1, 3:2, 4:3}
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
        return f(n)


n = 2
sol = Solution()
res = sol.fib(n)
print(res)
assert res == 1

n = 3
sol = Solution()
res = sol.fib(n)
print(res)
assert res == 2

n = 4
sol = Solution()
res = sol.fib(n)
print(res)
assert res == 3

n = 5
sol = Solution()
res = sol.fib(n)
print(res)
assert res == 5
