import math


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = math.inf
        max_profit = 0
        n = len(prices)

        for i in range(n):
            profit = prices[i] - min_price
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, profit)

        return int(max_profit)
