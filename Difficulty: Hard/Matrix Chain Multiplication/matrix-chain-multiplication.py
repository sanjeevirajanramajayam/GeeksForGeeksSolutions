class Solution:
    def matrixMultiplication(self, arr):
        # code here
        dp = {}
        def fn(i, j):
            if i == j:
                return 0
            steps = float('inf')
            if (i, j) in dp:
                return dp[(i, j)]
            for k in range(i, j):
                steps = min(steps, arr[i - 1] * arr[j] * arr[k] + fn(i, k) + fn(k + 1, j))
            dp[(i, j)] = steps
            return steps
        
        return fn(1, len(arr) - 1)