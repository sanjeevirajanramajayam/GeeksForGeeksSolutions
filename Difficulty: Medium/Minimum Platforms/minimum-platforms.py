class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        arr = sorted(arr)
        dep = sorted(dep)
        
        i = 0
        j = 0
        cnt = 0
        maxCnt = 0
        while i < len(arr) and j < len(dep):
            if arr[i] > dep[j]:
                # print(dep[j])
                cnt -= 1
                j += 1
            else:
                # print(arr[i])
                cnt += 1
                i += 1
            maxCnt = max(maxCnt, cnt)
        return maxCnt