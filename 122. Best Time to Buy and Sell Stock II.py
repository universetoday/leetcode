"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
-------------------------
Дан числовой массив, где prices[i] - это цена акции в i-ый день.

Каждый день ты можешь решать покупать и/или продавать акцию.
Ты можешь держать только одну акцию в любое время.
Тем не менее, ты можешь купить ее сразу после продажи в тот же день.

Вычисли максимальную прибыль.
-------------------------
MEDIUM
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            # Сравниваем две последовательные цены, если цена возросла, то добавляем разницу цен к максимальной прибыли.
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


prices = [7,1,5,3,6,4]
res = Solution().maxProfit(prices)
print(res)
assert res == 7

prices = [1,2,3,4,5]
res = Solution().maxProfit(prices)
print(res)
assert res == 4

prices = [7,6,4,3,1]
res = Solution().maxProfit(prices)
print(res)
assert res == 0
