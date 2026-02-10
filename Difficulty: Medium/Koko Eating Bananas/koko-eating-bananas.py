class Solution:
    def kokoEat(self, arr, k):
        # Code here
        def timeToEat(speed):
            time = 0
            for i in arr:
                time += math.ceil(i / speed)
            return (time)
        
        low = 1
        high = max(arr)
        
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if timeToEat(mid) > k:
                low = mid + 1
            elif timeToEat(mid) <= k :
                ans = mid
                high = mid - 1
        
        return ans