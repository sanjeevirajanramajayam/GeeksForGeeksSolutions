class Solution:
    def inversionCount(self, nums):
        # Code Here
        cnt = 0
        def merge(low, mid, high, nums):
            nonlocal cnt
            left = low
            right = mid + 1
            temp = []
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    cnt += mid - left + 1
                    right += 1
            while left <= mid:
                temp.append(nums[left])
                left += 1
            while right <= high:
                temp.append(nums[right])
                right += 1
            # print(low, mid, high)
            for i in range(low, high + 1):
                nums[i] = temp[i-low]

        def mergeSort(low, high, nums):
            if low >= high:
                return
            mid = (low + high) // 2
            mergeSort(low, mid, nums)
            mergeSort(mid + 1, high, nums)
            merge(low, mid, high, nums)
        
        mergeSort(0, len(nums) - 1, nums)
        return cnt