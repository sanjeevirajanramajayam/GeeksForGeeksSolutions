class Solution:
    def findKRotation(self, arr):
        # code here
        
        low = 0
        high = len(arr) - 1
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= arr[high]:
                high = mid - 1
                if arr[mid] < arr[ans]:
                    ans = mid
            elif arr[mid] >= arr[low]:
                if arr[low] < arr[ans]:
                    ans = low
                low = mid + 1
                
        
        return ans