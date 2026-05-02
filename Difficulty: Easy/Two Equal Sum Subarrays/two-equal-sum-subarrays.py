class Solution:
    def canSplit(self, arr):
        #code here
        sumArr = sum(arr)
        currSum = 0
        for i in range(len(arr)):
            currSum += arr[i]
            sumArr -= arr[i]
            if currSum == sumArr:
                return True
        return False