class Solution:
    def leaders(self, arr):
        # code here
        maxNow = float('-inf')
        ans = []
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= maxNow:
                ans.append(arr[i])
            maxNow = max(maxNow, arr[i])
        return sorted(ans, reverse=True)