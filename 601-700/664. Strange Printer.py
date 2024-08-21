"""
There is a strange printer with the following two special properties:

    The printer can only print a sequence of the same character each time.
    At each turn, the printer can print new characters starting from
    and ending at any place and will cover the original existing characters.

Given a string s, return the minimum number of turns the printer needed to print it.
-------------------------------

-------------------------------
HARD
"""


class Solution:
    def strangePrinter(self, s: str) -> int:

        n = len(s)
        a = [s[0]]
        for i in range(1, n):
            if s[i] != s[i - 1]:
                a.append(s[i])
        n = len(a)
        h = {}
        t = [n] * n
        for i in reversed(range(n)):
            if a[i] in h:
                t[i] = h[a[i]]
            h[a[i]] = i
        d = [[0] * n for _ in range(n + 1)]
        for i in range(n):
            d[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                d[i][j] = 1 + d[i + 1][j]
                k = t[i]
                while k <= j:
                    d[i][j] = min(d[i][j], d[i][k - 1] + d[k + 1][j])
                    k = t[k]
        return d[0][n - 1]


"""

"""

s = "aaabbb"
sol = Solution()
res = sol.strangePrinter(s)
print(res)
assert res == 2

s = "aba"
sol = Solution()
res = sol.strangePrinter(s)
print(res)
assert res == 2
