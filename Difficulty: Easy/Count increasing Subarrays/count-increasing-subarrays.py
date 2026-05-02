class Solution:
    def countIncreasing(self, nums):
        # code here.
        cnt = 0
        strk = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                strk += 1
            else:
                # print(strk)
                cnt += ((strk - 1) * strk) // 2
                strk = 1
        # print(strk)
        if strk > 0:
            cnt += ((strk - 1) * strk) // 2
        return cnt
            