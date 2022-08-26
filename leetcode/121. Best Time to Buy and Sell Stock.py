class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min_num, profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < min_num:
                min_num = prices[i]
            else:
                profit = max(prices[i] - min_num, profit)
        return profit
