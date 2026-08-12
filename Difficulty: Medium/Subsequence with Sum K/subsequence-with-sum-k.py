from functools import cache

class Solution:
    def checkSubsequenceSum(self, arr, k):

        @cache
        def fn(ind, target):
            if target == 0:
                return True

            if ind == 0:
                return arr[0] == target

            if arr[ind] <= target and fn(ind - 1, target - arr[ind]):
                return True

            return fn(ind - 1, target)

        return fn(len(arr) - 1, k)