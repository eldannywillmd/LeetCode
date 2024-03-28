class Solution:
    def maxProfit(self, prices):

        max_profit = 0
        lowest_price = prices[0]

        for day in range(1,len(prices)):
            if prices[day] < lowest_price:
                lowest_price = prices[day]
            max_profit_day = prices[day] - lowest_price
            if max_profit_day > max_profit:
                max_profit = max_profit_day

        return max_profit


prices = [900,2,9,300]

solution = Solution()
print(solution.maxProfit(prices))