class Solution:
    def maxProfit(self, prices):
        # code here
        l = 0
        r = l + 1
        profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
                # print(l, r, prices[l], prices[r])
            r += 1
        return profit
            