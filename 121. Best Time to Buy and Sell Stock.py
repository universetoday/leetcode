"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
-------------------
Задача: дан массив prices, где prices[i] — цена данной акции в i-й день.

Вам нужно максимизировать свою прибыль,
выбрав один день для покупки акции и другой день в будущем для продажи этой акции.

Верните максимальную прибыль, которую можно получить от этой транзакции.
Если прибыль не может быть получена, верните 0.
-------------------
EASY
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Если цен нет, то прибыль нулевая
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0
        # Итерация: проходим слева направо, находя минимальную цену
        for price in prices:
            if price < min_price:
                min_price = price
            # Потом проверяем прибыль относительно минимальной цены
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
sol = Solution()
res = sol.maxProfit(prices)
print(res)
assert res == 5

prices = [7, 6, 4, 3, 1]
sol = Solution()
res = sol.maxProfit(prices)
print(res)
assert res == 0
