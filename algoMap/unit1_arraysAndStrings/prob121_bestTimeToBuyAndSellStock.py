# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep track of current max profit and lowest price seen
        profit = 0
        min_seen = float('inf')
        
        # Iterate through all prices
        for price in prices:
            # If current price is lower than lowest seen so far, set it as new lowest
            if price < min_seen:
                min_seen = price
            
            # See what profit would be if sold this day, and set it if more than highest profit
            profit = max(profit, price - min_seen)
        
        return profit

prices = [7,1,5,3,6,4]    
# prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))