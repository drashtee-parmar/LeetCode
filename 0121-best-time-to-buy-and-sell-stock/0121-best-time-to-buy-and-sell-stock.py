class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Initialize variables
        min_price = float('inf')
        max_profit = 0
        
        # Iterate through each price
        for price in prices:
            # Update the min_price to be the smallest seen so far
            min_price = min(min_price, price)
            # Calculate the profit if selling at the current price
            profit = price - min_price
            # Update max_profit if the current profit is larger
            max_profit = max(max_profit, profit)
        
        return max_profit
        