"""
121 leetcode problem
"""

# Space complexity: O(1) - no extra space used
# Time complexity: O(n) - span through an array only once


prices_list = [7, 1, 5, 3, 6, 4]


def calc_max_profit(prices: list[int]) -> int:
    left, right = 0, 1  # left is buy, right is sell
    max_profit = 0

    while right < len(prices):
        # profitable transaction?
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:  # not profitable
            left = right
        right += 1  # regardless of the conditions, we need to shift the right pointer

    return max_profit
