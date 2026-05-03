class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        ans = 0
        hashmap = {0 : -1}
        currSum = 0
        for i in range(len(arr)):
            currSum += arr[i]
            if currSum - k in hashmap:
                ans = max(ans, i - hashmap[currSum - k])
            if currSum not in hashmap:
                hashmap[currSum] = i
        return ans
            
