from typing import List

class Solution:
    def maxProfit(self, max_transactions: int, prices: List[int]) -> int:
        number_of_days = len(prices)

        if number_of_days == 0 or max_transactions == 0:
            return 0

        if max_transactions >= number_of_days // 2:
            total_profit = 0
            for day in range(1, number_of_days):
                if prices[day] > prices[day - 1]:
                    total_profit += prices[day] - prices[day - 1]
            return total_profit

        buy_profit = [-float('inf')] * (max_transactions + 1)
        sell_profit = [0] * (max_transactions + 1)

        for current_price in prices:
            for transaction_count in range(1, max_transactions + 1):

                buy_profit[transaction_count] = max(
                    buy_profit[transaction_count],
                    sell_profit[transaction_count - 1] - current_price
                )

                sell_profit[transaction_count] = max(
                    sell_profit[transaction_count],
                    buy_profit[transaction_count] + current_price
                )

        return sell_profit[max_transactions]