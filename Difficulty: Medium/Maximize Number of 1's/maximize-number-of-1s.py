class Solution:
    def maxOnes(self, arr, k):
        # code here
        l = 0
        replacements = 0
        maxLen = 0
        for r in range(len(arr)):
            if arr[r] == 0:
                replacements += 1
            
            while replacements > k:
                if arr[l] == 0:
                    replacements -= 1
                l += 1
                
            # print([arr[i] for i in range(l, r+1)])
            
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
        