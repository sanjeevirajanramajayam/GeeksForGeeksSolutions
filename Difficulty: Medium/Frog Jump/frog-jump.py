class Solution:
    def minCost(self, height):
        # code here
        dp = [-1] * (len(height) + 1)
        def fn(i):
            if i == 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            left = fn(i - 1) +  abs(height[i] - height[i - 1])
            right = float('inf')
            if i > 1:
                right = fn(i - 2) + abs(height[i] - height[i - 2])
            dp[i] = min(left, right)
            return dp[i]
        
        return fn(len(height) - 1)