class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        maxi = float('-inf')
        currSum = 0
        start = 0
        for i in range(len(arr)):
            currSum += arr[i]
            if maxi < currSum:
                maxi = currSum
                end = i
            if currSum < 0:
                currSum = 0
                start = i
        # print(arr[start:end + 1])
        return maxi