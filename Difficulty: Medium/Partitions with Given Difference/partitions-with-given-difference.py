class Solution:
    def countPartitions(self, arr, diff):
        # code here
        totSum = sum(arr)
        if not( (totSum - diff) >= 0 and ((totSum - diff) % 2 == 0) ):
            return 0
        csum = totSum - diff
        csum //= 2
        
        dp = [[-1 for j in range(csum + 2)] for i in range(len(arr))]
        
        def find_count(ind, csum):
            if ind == 0:
                if arr[0] == 0 and csum == 0:
                    return 2
                if arr[0] == csum:
                    return 1
                if csum == 0:
                    return 1
                return 0
            if dp[ind][csum] != -1:
                return dp[ind][csum]
            take = 0
            if arr[ind] <= csum:
                take = find_count(ind - 1, csum - arr[ind])
            not_take = find_count(ind - 1, csum)
            dp[ind][csum] = take + not_take
            return take + not_take
        
        return find_count(len(arr) - 1, csum);