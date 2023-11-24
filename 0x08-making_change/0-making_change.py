#!/usr/bin/python3
""" make change module """

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the table with a value larger than any possible solution
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make amount 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still the initial value, total cannot be achieved
    return dp[total] if dp[total] != float('inf') else -1
