class Solution:
    def knapSack(self, val, wt, capacity):
        dp = [0] * (capacity + 1)

        for i in range(len(wt)):
            for c in range(wt[i], capacity + 1):
                dp[c] = max(dp[c], val[i] + dp[c - wt[i]])

        return dp[capacity]