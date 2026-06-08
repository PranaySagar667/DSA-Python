"""
Problem: Best Time to Buy and Sell Stock (LeetCode #121)
Find the maximum profit from one buy-sell transaction.

Approach: Track minimum price seen so far, update max profit
Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:

        if price < min_price:
            min_price = price
        
        elif price - min_price > max_profit:
            max_profit = price - min_price 
            
    return max_profit


# ---- Test ----
print(max_profit([7, 1, 5, 3, 8, 4]))  # 7
print(max_profit([7, 6, 4, 3, 1]))     # 0 