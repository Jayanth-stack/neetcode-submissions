class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buyPrice = prices[0]
        if not prices:
            return 0

        for price in prices[1:]:
            profit_cal = price - buyPrice
            max_profit = max(max_profit, profit_cal)
            buyPrice = min(buyPrice, price)
        
        
        

        return max_profit 
