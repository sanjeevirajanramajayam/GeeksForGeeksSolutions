class Solution:
    def longestBitonicSequence(self, n, nums):
        # code here
        dp = [1] * len(nums)
        maxi = float('-inf')
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        
        dp2 = [1] * len(nums)
        nums.reverse()
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp2[j] + 1 > dp2[i]:
                        dp2[i] = dp2[j] + 1
        dp2.reverse()
        
        maxi = 0
        for i in range(n):
            if dp[i] > 1 and dp2[i] > 1: 
                maxi = max(maxi, dp[i] + dp2[i] - 1)
        return maxi