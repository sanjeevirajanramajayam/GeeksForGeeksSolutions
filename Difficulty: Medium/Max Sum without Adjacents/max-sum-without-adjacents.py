#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
	    dp = [-1] * (n + 1)
	    
        def fn(ind):
            if (ind == 0):
                return arr[0]
            if ind < 0:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            take = fn(ind - 2) + arr[ind]
            not_take = fn(ind - 1) 
            dp[ind] = max(take, not_take)
            return dp[ind]
        
        return fn(n - 1)