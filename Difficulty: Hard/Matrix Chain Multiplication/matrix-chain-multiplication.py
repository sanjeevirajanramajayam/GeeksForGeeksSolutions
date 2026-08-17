from functools import cache
class Solution:
    def matrixMultiplication(self, arr):
        # code here
        @cache
        def mcm(i, j):
            if i == j:
                return 0
            mini = float('inf')
            for k in range(i, j):
                steps = arr[i - 1] * arr[k] * arr[j] + mcm(i, k) + mcm(k + 1, j) 
                mini = min(mini, steps)
            return mini
        return mcm(1, len(arr) - 1)