class Solution:
    def maxProfit(self, prices):

        max_profit = 0
        buffer = -2

        for i in range(1, len(prices)):
            if prices[i] < prices[i-1] and buffer > 0:
                buffer = prices[i]
            if buffer == -1:
                buffer = 0
            if prices[i] > prices[i-1]:
                if buffer == -2:
                    buffer = 0
                max_profit += prices[i] - prices[i - 1] - buffer
                print(max_profit)
                buffer = -1
        return max_profit

    def maxProfit2(self, prices):

        total_profit = 0
        n = len(prices)

        for i in range(n - 1):
            j = i + 1

            if prices[j] > prices[i]:
                total_profit += (prices[j] - prices[i])

        return total_profit



prices = [1,7,4,2,11]
solution = Solution()
print(solution.maxProfit2(prices))