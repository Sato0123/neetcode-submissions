class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
                # print(i, j, profit, max_profit)

        return max_profit
