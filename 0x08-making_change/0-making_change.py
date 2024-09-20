#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    
    Args:
        coins (list of ints): List of coin denominations.
        total (int): The total amount to be met with the fewest coins.
        
    Returns:
        int: Fewest number of coins needed to meet total, or -1 if it is not possible.
    """
    if total <= 0:
        return 0
    
    # Initialize the dp array to track the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make a total of 0
    
    # Iterate over each coin
    for coin in coins:
        # Update dp array for all amounts that can be made using the current coin
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
