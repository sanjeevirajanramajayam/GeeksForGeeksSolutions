#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        dp = [[-1 for i in range(len(price) + 2)] for j in range(len(price) + 2)]
        def fn(ind, N):
            if ind == 0:
                return N * price[0]
            if dp[ind][N] != -1:
                return dp[ind][N]
            take = 0
            if N >= ind + 1:
                take = price[ind] + fn(ind, N - (ind + 1))
            not_take = fn(ind - 1, N)
            dp[ind][N] = max(take, not_take)
            return max(take, not_take)
            
        for i in range(len(price) + 2):
            dp[0][i] = i * price[0]
        
        for i in range(1, len(price)):
            for j in range(len(price) + 1):
                take = 0
                if j >= i + 1:
                    take = price[i] + dp[i][ j - (i + 1)]
                not_take = dp[i - 1][j]
                dp[i][j] = max(take, not_take)
                
        
        return dp[len(price) - 1][len(price)]