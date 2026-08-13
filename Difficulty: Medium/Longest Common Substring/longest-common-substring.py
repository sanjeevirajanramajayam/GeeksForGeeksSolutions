class Solution:
    def longCommSubstr(self, s1, s2):
        # code here
        dp = [[0 for i in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        ans = float('-inf')
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
        if ans == float('-inf'):
            return 0
        return ans