class Solution:
    def minDifference(self, arr: list[int]) -> int:

        total = sum(arr)

        dp = [False] * (total + 1)
        dp[0] = True

        for num in arr:
            for j in range(total, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        ans = float('inf')

        for i in range(total // 2 + 1):
            if dp[i]:
                ans = min(ans, total - 2 * i)

        return ans