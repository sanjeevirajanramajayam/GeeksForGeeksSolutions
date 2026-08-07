class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        arr.sort()
        def cowCnt(minDist):
            last = arr[0]
            cows = 1
            currDist = 0
            for i in range(1, len(arr)):
                currDist = arr[i] - last
                if currDist >= minDist:
                    cows += 1
                    currDist = 0
                    last = arr[i]
            return cows
        
        low = 1
        high = max(arr) - min(arr)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            # print(cowCnt(mid), mid)
            # print(low, high, mid, cowCnt(mid))
            if cowCnt(mid) >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans