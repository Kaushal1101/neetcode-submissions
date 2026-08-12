class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        best_profit = 0

        for i in range(1, len(prices)):
            sell_profit = prices[i] - buy_price
            best_profit = max(best_profit, sell_profit)

            buy_price = min(buy_price, prices[i])
            

        return best_profit