from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

prices = [7, 1, 5, 3, 6, 4]

solution = Solution()
result = solution.maxProfit(prices)

print("Maximum profit:", result)