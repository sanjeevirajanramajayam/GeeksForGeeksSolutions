class Solution:
    def longestBitonicSequence(self, n, nums) -> int:
        # code here
        
        dp1 = [1 for i in range(len(nums))]
        dp2 = [1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i] and dp1[j] + 1 > dp1[i]:
                    dp1[i] = dp1[j] + 1
        
        nums = nums[::-1]
        
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i] and dp2[j] + 1 > dp2[i]:
                    dp2[i] = dp2[j] + 1
        dp2 = dp2[::-1]
        dp3 = [0 for i in range(len(nums))]
        
        for i in range(len(nums)):
            if dp1[i] > 1 and dp2[i] > 1:
                
                dp3[i] = dp1[i] + dp2[i] - 1
        # print(dp3)
        return max(dp3)