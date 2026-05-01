class Solution:
    def maxLength(self, arr):
        # code here
        currentSum = 0
        ans = 0
        prefixHash = {}
        for i in range(len(arr)):
            currentSum += arr[i]
            if currentSum == 0:
                ans = max(ans, i + 1)
            elif currentSum in prefixHash:
                ans = max(i - prefixHash[currentSum], ans)
            else:
                prefixHash[currentSum] = i
        return ans
        