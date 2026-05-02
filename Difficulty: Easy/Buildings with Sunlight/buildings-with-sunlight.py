class Solution:
    def visibleBuildings(self, arr):
        # code here
        currentMax = float('-inf')
        cnt = 0
        for i in range(len(arr)):
            if arr[i] >= currentMax:
                currentMax = arr[i]
                cnt += 1
        return cnt