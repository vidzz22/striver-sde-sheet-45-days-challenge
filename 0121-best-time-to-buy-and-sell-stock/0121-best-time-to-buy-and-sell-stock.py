class Solution(object):
    def maxProfit(self, prices):

        # Lowest buying price seen so far
        min_price = prices[0]

        # Best profit achievable
        max_profit = 0

        for price in prices:

            min_price = min(min_price, price)

            # Profit if we sell today
            max_profit = max(max_profit, price - min_price)

        return max_profit