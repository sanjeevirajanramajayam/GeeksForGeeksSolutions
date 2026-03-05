class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        l = 0
        freqMap = {}
        maxLen = -1
        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            while len(freqMap) > k:
                freqMap[s[l]] -= 1
                if freqMap[s[l]] == 0:
                    del freqMap[s[l]]
                l += 1
            if len(freqMap) == k:
                maxLen = max(maxLen, r - l + 1)
        return maxLen