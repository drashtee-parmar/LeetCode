class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Step 1: Initialize DP array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case
        
        # Step 2: Fill DP array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Step 3: Return result
        return dp[amount] if dp[amount] != float('inf') else -1