class Solution:
    def isSubsetSum (self, arr, target):
        # code here 
        dp = [[-1 for i in range(target + 1)] for j in range(len(arr) + 1)]
        def fn(ind, target):
            if target == 0:
                return True
            if ind == 0:
                return target == arr[ind]

            
            if dp[ind][target] != -1:
                return dp[ind][target]
            
            take = False
            if target >= arr[ind]:
                take = fn(ind - 1, target - arr[ind])
        
            not_take = fn(ind - 1, target)
            dp[ind][target] = take or not_take
            return take or not_take
        
        return fn(len(arr) - 1, target)